# Contributing to 3aransia

Hi! Thanks for your interest in contributing to [3aransia](http://3aransia.com/).
You'll be joining a [long list of contributors](https://github.com/3aransia/3aransia/blob/master/AUTHORS.md).
In this document we'll try to summarize everything that you need to know to
do a good job.


## Code and Issues

We use [GitHub](https://www.github.com/) to host our code repositories and
issues. The [3aransia organization on GitHub](https://github.com/3aransia) has many
repositories, so we can manage better the issues and development. The most
important are:

- [3aransia/3aransia](https://github.com/3aransia/3aransia/), the main repository with code
  related to the library;
- [3aransia/3aransia.github.com](https://github.com/3aransia/3aransia.github.com), 3aransia website
  with information about the library, documentation, link for downloading 3aransia etc.;


## Development priorities

3aransia consists of the functionality that the Python/NLP community is motivated to contribute.
Some priority areas for development are listed in the [3aransia Wiki](https://github.com/3aransia/3aransia/wiki)

## Git and our Branching model

### Git

We use [Git](http://git-scm.com/) as our [version control
system](http://en.wikipedia.org/wiki/Revision_control), so the best way to
contribute is to learn how to use it and put your changes on a Git repository.
There's a plenty of documentation about Git -- you can start with the [Pro Git
book](http://git-scm.com/book/).


### Setting up a Development Environment

To set up your local development environment for contributing to the main
repository [3aransia/3aransia](https://github.com/3aransia/3aransia/):

- Fork the [3aransia/3aransia](https://github.com/3aransia/3aransia/) repository on GitHub
  to your account;
- Clone your forked repository locally
  (`git clone https://github.com/<your-github-username>/3aransia.git`);
- Run `cd 3aransia` to get to the root directory of the `3aransia` code base;
- Install the dependencies (`pip install -r requirements.txt`);
- Download the datasets for running tests
  (`python -m 3aransia.downloader all`);
- Create a remote link from your local repository to the
  upstream `3aransia/3aransia` on GitHub
  (`git remote add 3aransia https://github.com/3aransia/3aransia.git`) --
  you will need to use this `3aransia` link when updating your local repository
  with all the latest contributions.

### GitHub Pull requests

We use the famous
[gitflow](http://nvie.com/posts/a-successful-git-branching-model/) to manage our
branches.

Summary of our git branching model:
- Go to the `develop` branch (`git checkout develop`);
- Get all the latest work from the upstream `3aransia/3aransia` repository
  (`git pull upstream develop`);
- Create a new branch off of `develop` with a descriptive name (for example:
  `feature/latin_digit_moroccan-arabic-mapping`, `hotfix/bug-on-downloader`). You can
  do it switching to `develop` branch (`git checkout develop`) and then
  creating a new branch (`git checkout -b name-of-the-new-branch`);
- Do many small commits on that branch locally (`git add files-changed`,
  `git commit -m "Add some change"`);
- Run the tests to make sure nothing breaks
- **Add your name to the `AUTHORS.md` file as a contributor**;
- Push to your fork on GitHub (with the name as your local branch:
  `git push origin branch-name`);
- Create a pull request using the GitHub Web interface (asking us to pull the
  changes from your new branch and add to our `develop` branch);
- Wait for comments.


### Tips

- Write [helpful commit
  messages](http://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message).
- Anything in the `develop` branch should be deployable (no failing tests).
- Never use `git add .`: it can add unwanted files;
- Avoid using `git commit -a` unless you know what you're doing;
- Check every change with `git diff` before adding them to the index (stage
  area) and with `git diff --cached` before commiting;
- Make sure you add your name to our [list of contributors](https://github.com/3aransia/3aransia/blob/master/AUTHORS.md);
- If you have push access to the main repository, please do not commit directly
  to `develop`: your access should be used only to accept pull requests; if you
  want to make a new feature, you should use the same process as other
  developers so you code will be reviewed.


## Code Guidelines

- Use [PEP8](http://www.python.org/dev/peps/pep-0008/);
- Write tests for your new features (please see "Tests" topic below);
- Always remember that [commented code is dead
  code](http://www.codinghorror.com/blog/2008/07/coding-without-comments.html);
- Name identifiers (variables, classes, functions, module names) with readable
  names (`x` is always wrong);
- When manipulating strings, use [Python's new-style
  formatting](http://docs.python.org/library/string.html#format-string-syntax)
  (`'{} = {}'.format(a, b)` instead of `'%s = %s' % (a, b)`);
- All `#TODO` comments should be turned into issues (use our
  [GitHub issue system](https://github.com/3aransia/3aransia/issues));
- Run all tests before pushing so you will know if your
  changes broke something;

See also our [developer's
guide](https://github.com/3aransia/3aransia/wiki/Developers-Guide).


## Tests

You should write tests for every feature you add or bug you solve in the code.
Having automated tests for every line of our code let us make big changes
without worries: there will always be tests to verify if the changes introduced
bugs or lack of features. If we don't have tests we will be blind and every
change will come with some fear of possibly breaking something.

For a better design of your code, we recommend using a technique called
[test-driven development](https://en.wikipedia.org/wiki/Test-driven_development),
where you write your tests **before** writing the actual code that implements
the desired feature.
 

# Discussion 

We have three disscussion plateforms:

- [3aransia Messenger][3aransia Messenger] for real-time discussions and annoucements;
- [3aransia Facebook Group][3aransia Facebook Group] for annoucements and community support;
- [3aransia Slack][3aransia Slack] for feature developments and thread support in channels.

Please feel free to contact us through the 3aransia@3aransia.com mail if
you have any questions or suggestions. Every contribution is very welcome!

Happy hacking! (;

[3aransia Messenger]: https://m.me/join/AbYiiixcEQfGO6Cw
[3aransia Facebook Group]: https://www.facebook.com/groups/3aransia
[3aransia Slack]: 3aransia.slack.com
