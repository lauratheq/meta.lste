# LSTE Plugin: Meta Field Processor

This plugin for [Lauras Simple Template Engine (LSTE)](https://github.com/lauratheq/lste) processes content by extracting and removing meta fields. Meta fields are defined within your content using the pattern `{{field:value}}`. This plugin allows you to manage and replace these fields dynamically, making your content more modular and adaptable.

## Usage

### Installation

1. Add the plugin to your LSTE configuration by including it in your `.listerc` file:

    ```ini
    [plugins]
    meta-fields = lauratheq/meta-fields.lste
    ```

2. LSTE will automatically download and activate the plugin during the next site generation.

### Configuration

To use the Meta Field Processor plugin, include meta fields in your content files (e.g., `about.md`) using the `{{field:value}}` syntax.

#### Example Content File (`about.md`)

```markdown
{{title: About Us}}
{{description: Learn more about our company and values.}}

# About Us

We are a company committed to excellence...
```

#### Template Integration

In your HTML templates, you can reference these meta fields using the {{field}} syntax:

```html
<head>
    <title>{{title}}</title>
    <meta name="description" content="{{description}}">
</head>
<body>
    <h1>{{title}}</h1>
    <p>{{description}}</p>
</body>
```

### Advanced Usage

You can define any number of meta fields in your content files, and these will be extracted and replaced accordingly. This enables you to create dynamic and customizable templates with minimal effort.

## Contributing

### Contributor Code of Conduct

Please note that this project is adapting the [Contributor Code of Conduct](https://learn.wordpress.org/online-workshops/code-of-conduct/) from WordPress.org even though this is not a WordPress project. By participating in this project you agree to abide by its terms.

### Basic Workflow

* Grab an issue
* Fork the project
* Add a branch with the number of your issue
* Develop your stuff
* Commit to your forked project
* Send a pull request to the main branch with all the details

Please make sure that you have [set up your user name and email address](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) for use with Git. Strings such as `silly nick name <root@localhost>` look really stupid in the commit history of a project.

Due to time constraints, you may not always get a quick response. Please do not take delays personally and feel free to remind.

### Workflow Process

* Every new issue gets the label 'Request'
* Every commit must be linked to the issue with following pattern: `#${ISSUENUMBER} - ${MESSAGE}`
* Every PR only contains one commit and one reference to a specific issue
