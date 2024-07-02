<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">FILTERLESSCOOK</h1>
</p>
<p align="center">
    <em>Cook, Collab, Code-Repeat! This slogan encapsulates the project's purpose (creating food recipes), values flexibility for collaboration (open-source community), and encourages repeat usage with the simplicity of repeat. It doesn't include the exact project name but alludes to it indirectly through the actions performed by the user (cook, collaborate, code).</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/Bissbert/filterlesscook?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Bissbert/filterlesscook?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Bissbert/filterlesscook?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Bissbert/filterlesscook?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

FilterlessCook is an open-source project designed to streamline culinary documentation. Powered by Python and the ollama library, it offers a simple tool (recipe-generator) that produces well-structured LaTeX formatted recipes for various dishes. The project emphasizes flexibility and collaboration with its permissive licensing model. With custom prompt support, users can effortlessly create unique food-focused documents while maintaining the high quality and consistency expected in FilterlessCooks ecosystem. This innovative approach encourages culinary creativity within the broader software development community.

---

##  Features

|    |   Feature         | Description                                                                               |
|----|-------------------|--------------------------------------------------------------------------------------------|
| ⚙️  | **Architecture**  | Python project using a simple CLI tool (recipe-generator) built with ollama library, leveraging LaTeX for recipe formatting.                                            |
| 🔩 | **Code Quality**  | Modular design with well-named functions and classes, consistent indentation, clear comments, and use of docstrings. Following PEP8 style guide.                       |
| 📄 | **Documentation** | Includes README.md for project overview, LISENCE for permissive licensing, detailed setup instructions in `setup.py`, and documentation within codebase (docstrings).  |
| 🔌 | **Integrations**  | Utilizes ollama library to interact with users and generate recipes, with a potential integration of other NLP tools.                                              |
| 🧩 | **Modularity**    | Clear separation of concerns among `filterlesscook/`, `recipes/` and other directories, making the codebase reusable for similar projects.                          |
| 🧪 | **Testing**       | Not observed within the provided repository. Potential testing using Python's built-in `unittest`.                                                                         |
| ⚡️  | **Performance**   | Low computational requirements as it processes text-based data, but resource usage will depend on the complexity of user inputs and ollama library performance.      |
| 🛡️ | **Security**      | Does not process sensitive data; however, a secure environment for running the ollama model is necessary to ensure privacy compliance.                          |
| 📦 | **Dependencies**  | Python>=3.7, requests, ollama, tabulate, rich, pydantic, and python-dotenv packages.                                                                           |

---

##  Repository Structure

```sh
└── filterlesscook/
    ├── LISENCE
    ├── MANIFEST.in
    ├── filterlesscook
    │   ├── __init__.py
    │   └── filterlesscook.py
    └── setup.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                              | Summary                                                                                                                                                                                                                                                                                                                               |
| ---                                                                               | ---                                                                                                                                                                                                                                                                                                                                   |
| [MANIFEST.in](https://github.com/Bissbert/filterlesscook/blob/master/MANIFEST.in) | In this open-source repository named FilterlessCook, the MANIFEST.in file ensures crucial documentation-the README.md and license (LISENCE) – is included during package installation. This facilitates project understanding and promotes reusability within the software ecosystem.                                                 |
| [setup.py](https://github.com/Bissbert/filterlesscook/blob/master/setup.py)       | The provided `setup.py` file initializes the RecipeGenerator, a Python-3.7 tool that leverages the ollama library to create LaTeX formatted food recipes. With an easy-to-use console script named recipe-generator, it's accessible for developers and simplifies the process of generating well-structured culinary documentation.  |
| [LISENCE](https://github.com/Bissbert/filterlesscook/blob/master/LISENCE)         | This License file, part of FilterlessCook, outlines permissive use rights for the software contained within. It ensures freedom to use, modify, distribute, or even sell this codebase while maintaining its original copyright ownership. Essentially, it fosters a vibrant developer community with shared purpose and flexibility. |

</details>

<details closed><summary>filterlesscook</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                          | ---                                                                                                                                                                                                                                                                                                        |
| [filterlesscook.py](https://github.com/Bissbert/filterlesscook/blob/master/filterlesscook/filterlesscook.py) | Empowers users to generate LaTeX formatted recipes for specific food items, leveraging the ollama library for chat interaction. Users can define custom prompts and specify an output file path. This tool facilitates easy recipe creation within the `filterlesscook` open-source projects architecture. |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version x.y.z`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the filterlesscook repository:
>
> ```console
> $ git clone https://github.com/Bissbert/filterlesscook
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd filterlesscook
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run filterlesscook using the command below:
> ```console
> $ python main.py
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/Bissbert/filterlesscook/issues)**: Submit bugs found or log feature requests for the `filterlesscook` project.
- **[Submit Pull Requests](https://github.com/Bissbert/filterlesscook/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Bissbert/filterlesscook/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Bissbert/filterlesscook
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/Bissbert/filterlesscook/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Bissbert/filterlesscook">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
