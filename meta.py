#!/usr/bin/python3

"""
This script processes content by extracting and removing meta fields. 
Meta fields are identified by the pattern {{field:value}} within the content.

The script includes the following functions:
- `register_hooks`: Registers hooks for processing content.
- `load_meta_fields`: Extracts meta fields from the content and updates the content.
- `extract_and_remove_meta_fields`: Extracts meta fields using regex and removes them from the content.
- `replace_meta_fields`: Replaces meta fields in the content based on a dictionary of meta fields.
- `replace_field`: Replaces occurrences of a specific fieldname with its corresponding value.
- `replace_fields`: Replaces all meta fields in the content with their corresponding values.

Legal Note:
 - Written and maintained by Laura Herzog (laura-herzog@outlook.com)
 - Licensed under the GPL license. See the project at https://github.com/lauratheq/lste
"""

import re
from typing import Dict, Any, Tuple

def register_hooks(lste: Any) -> None:
    """
    Registers hooks to process content when the 'load_content' event occurs and
    to replace meta fields before loading custom functions.

    Args:
        lste: An object that supports hook registration. It will call `load_meta_fields`
              when the 'load_content' hook is triggered and `replace_meta_fields` 
              when the 'single_content' hook is triggered.
    """
    lste.hooks.add('load_content', load_meta_fields)
    lste.hooks.add('single_content', replace_meta_fields)
    lste.hooks.add('pre_load_custom_functions', replace_meta_fields)

def load_meta_fields(content: Dict[str, Dict[str, str]]) -> Dict[str, Dict[str, str]]:
    """
    Extracts and removes meta fields from each file's content in the provided dictionary.

    Args:
        content (dict): A dictionary where each key represents a file and the value is 
                        a dictionary containing 'content' and 'meta' fields. The 'content'
                        field is a string of the file's content.

    Returns:
        dict: The updated dictionary with extracted meta fields added under the 'meta' key
              and the cleaned content under the 'content' key.
    """
    for file in content:
        file_content = content[file]['content']
        meta_fields, file_content = extract_and_remove_meta_fields(file_content)
        if 'meta' not in content[file]:
            content[file]['meta'] = {}
        content[file]['meta'].update(meta_fields)
        content[file]['content'] = file_content

    return content

def extract_and_remove_meta_fields(content: str) -> Tuple[Dict[str, str], str]:
    """
    Extracts meta fields from the content using a regex pattern and removes them from the content.

    Args:
        content (str): A string of content from which meta fields need to be extracted and removed.

    Returns:
        tuple: A dictionary of extracted meta fields where the key is the field name and the
               value is the field value, and the cleaned content with meta fields removed.
    """
    # Regular expression to match {{field:value}}
    pattern = r'\{\{([\w-]+):([^}]*)\}\}'
    
    # Find all matches in the content string
    matches = re.findall(pattern, content)
    
    # Convert list of tuples to dictionary
    meta_dict = {field.strip(): value.strip() for field, value in matches}
    
    # Remove meta fields from content
    content_without_meta = re.sub(pattern, '', content).strip()
    
    return meta_dict, content_without_meta

def replace_meta_fields(content: str, file: str, lste: Any) -> str:
    """
    Replaces meta fields in the content based on the meta fields associated with a specific file.

    Args:
        content (str): The content in which meta fields need to be replaced.
        file (str): The filename to lookup meta fields.
        lste: An object that contains the content dictionary with meta fields.

    Returns:
        str: The content with meta fields replaced by their corresponding values.
    """
    meta_fields = lste.content[file]['meta']
    content = replace_fields(content, meta_fields)

    return content

def replace_field(content: str, fieldname: str, value: str) -> str:
    """
    Replaces occurrences of a specific fieldname in the content with its corresponding value.

    Args:
        content (str): The content in which the fieldname needs to be replaced.
        fieldname (str): The name of the field to replace.
        value (str): The value to replace the fieldname with.

    Returns:
        str: The content with the specific fieldname replaced by its value.
    """
    # Create a pattern to match {{fieldname}} with properly escaped curly braces
    pattern = re.escape('{{' + fieldname + '}}')
    
    # Replace occurrences of the fieldname with its value
    return re.sub(pattern, value, content)

def replace_fields(content: str, meta_fields: Dict[str, str]) -> str:
    """
    Replaces all meta fields in the content with their corresponding values.

    Args:
        content (str): The content in which meta fields need to be replaced.
        meta_fields (dict): A dictionary where keys are field names and values are field values.

    Returns:
        str: The content with all meta fields replaced by their corresponding values.
    """
    # Trim whitespace from meta field values
    trimmed_meta_fields = {k: v.strip() for k, v in meta_fields.items()}
    
    for fieldname, value in trimmed_meta_fields.items():
        content = replace_field(content, fieldname, value)
    return content
