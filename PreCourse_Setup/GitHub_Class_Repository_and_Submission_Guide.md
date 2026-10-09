# GitHub Class Repository and Submission Guide

Reusable across classes | October 9, 2026

**Use one public repository per class, not one per assignment.**
Choose one setup method below. If your class repository already exists,
skip setup and use the assignment/submission sections.

## Before You Start

Have your GitHub account, Git installed, and your instructor's GitHub username.
Commands below use PowerShell in your editor's terminal. Run each command
separately; stop if one fails. Replace example paths, YOUR-USERNAME, and
CLASS-REPO with your values. Do not type placeholder angle brackets.

Check Git and your commit identity:

```powershell
git --version
git config --global user.name
git config --global user.email
```

If your identity is missing, set it:

```powershell
git config --global user.name "Your Name"
git config --global user.email "YOUR-GITHUB-COMMIT-EMAIL"
```

Use your GitHub-provided no-reply email if you do not want your personal address
in public commits. Never commit passwords, API keys, or private student data.

## Method 1: GitHub First, Then Clone

### Create the Class Repository

1. Sign in to GitHub. Select the **+** menu, then **New repository**.
2. Choose your personal account as **Owner**.
3. Enter your instructor's class repository name, such as `119_Algorithmic_Problem_Solving`.
4. Choose **Public**.
5. Enable the README option. This gives the repository its first file.
6. Leave license and gitignore selections unset unless instructed otherwise.
7. Click **Create repository**.

[Screenshot placeholder: new repository form with Owner, name, Public, and README.]

See [GitHub: creating a repository](https://docs.github.com/en/get-started/start-your-journey/creating-a-repository-for-your-project-on-github).

### Add Your Instructor as Collaborator

1. Open the repository on GitHub.
2. Click **Settings**; if hidden, look in the repository's tab overflow menu.
3. Under **Access**, select **Collaborators**. Authenticate again if prompted.
4. Click **Add people**.
5. Search for the instructor's supplied GitHub username and select the correct account.
6. Confirm **Add [name] to [repository]**.
7. Check the invitation status. Access begins when the instructor accepts.

[Screenshot placeholder: Collaborators page and invitation status.]

These steps also apply in Method 2. See [GitHub: inviting collaborators](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository).

### Clone Onto Your Machine

1. On the repository's main page, click **Code**, choose **HTTPS**, and copy the URL.
2. Open a terminal in an existing parent folder where you keep class projects,
   not inside another Git repository.
3. Clone and enter the new folder:

```powershell
cd "D:\Coding_Projects"
git clone https://github.com/YOUR-USERNAME/CLASS-REPO.git
cd CLASS-REPO
git status
git remote -v
```

4. Open that cloned folder in your editor. Confirm the README exists and
   `git remote -v` names your class repository. Do not run `git init` again.

[Screenshot placeholder: Code/HTTPS copy button and successful local clone.]

A ZIP download is not a connected clone. See [GitHub: cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

## Method 2: Local App First, Then Connect GitHub

### Create the Local Class Folder and App

1. Create a class folder in File Explorer, outside any other repository.
2. Open that folder in your editor.
3. Create `week_01/AL01` (or the folder your instructor specifies).
4. Place your application and assignment README there; test it.
5. At the class-folder root, create a short README identifying the class.
6. Create a root `.gitignore` before staging. For example:

```gitignore
__pycache__/
*.pyc
.venv/
node_modules/
.env
.env.*
!.env.example
```

Do not ignore required source/data files. An example environment file must contain
placeholders, not secrets. If an app already exists, copy its files into the
assignment folder, not its `.git` directory.

### Initialize and Commit Locally

Open the terminal at the **class-folder root**, not the assignment folder:

```powershell
cd "D:\Coding_Projects\CLASS-REPO"
git status
```

For a new folder, "not a git repository" is expected. If Git instead reports
an existing repository, check its root with `git rev-parse --show-toplevel`;
do not initialize inside another repository.

For a confirmed new class folder:

```powershell
git init -b main
git status
git add .
git diff --cached --stat
git commit -m "Add initial class work"
```

Review staged files before committing. If Git requests your name/email, complete
the identity setup above and retry the commit.

### Create the Empty GitHub Repository

1. On GitHub, select **+**, then **New repository**.
2. Choose your personal account, the class name, and **Public**.
3. **Do not initialize with a README, gitignore, or license** for this method.
4. Click **Create repository** and copy its HTTPS URL from the setup page.

[Screenshot placeholder: empty repository form and HTTPS setup URL.]

### Connect and Push

In the local class-folder terminal:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/CLASS-REPO.git
git remote -v
git push -u origin main
```

Refresh GitHub and check the files. If prompted, follow the browser/credential
manager sign-in process. A GitHub account password is not used as an HTTPS Git
password. For "origin already exists" or a rejected push, ask for help; do not
force-push or delete work.

[Screenshot placeholder: remote verification and first successful push.]

The empty remote avoids conflicting initial histories.
See [GitHub: adding local code](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github).

### Add the Instructor

Use **Settings > Collaborators > Add people**, as detailed in Method 1.
Confirm the correct username and invitation status.

## Organize and Update Assignments

Use the instructor's folder names. Example:

```text
CLASS-REPO/
  README.md
  .gitignore
  week_01/
    AL01/
      main.py
      ticket_data.py
      test_assignment.py
      README.md
  week_02/
    AL02/
      ...
```

Each assignment folder must contain its complete runnable solution and needed
support files. Add new weeks inside this existing repository; do not create
another class repository or run `git init` in weekly folders.

For a later graded iteration, copy the previous solution into the new designated
folder. Keep the earlier submitted version intact for grading. Ordinary daily
progress within a single assignment uses commits in the same working folder.

After saving and testing, commit/push from the class root. Substitute the actual
assignment path:

```powershell
git status
git add week_01/AL01
git diff --cached --stat
git commit -m "Complete Week 1 AL01"
git push
```

Stage any required root-file changes separately. If there are no changes,
a new commit is unnecessary. A local commit alone is not a GitHub submission.

[Screenshot placeholder: local folder layout and files visible on GitHub.]

## Paired Assignments

Develop in the separate shared assignment repository. Each member then copies
the agreed complete files into their own class repository, adds individual
README notes, tests the destination copy, and commits/pushes.

Do not copy the shared repo's `.git` folder or add partners to your class repo.
Follow [the paired programming guide](Paired_Programming_and_Assignment_Submission_Guide.md) for roles and handoffs.

## Submit in Schoology

1. Refresh **your own class repository** on GitHub.
2. Open the assignment folder; confirm source, dependencies, and updated README
   are visible and complete.
3. Copy your class repository's browser URL:
   `https://github.com/YOUR-USERNAME/CLASS-REPO`.
4. Open the corresponding Schoology assignment and its submission area.
5. Paste **your class repository URL, not a shared paired-work URL**.
6. Identify the folder, such as `week_01/AL01`, in the submission message.
7. Complete Schoology's submission action and confirm it shows as submitted.

[Screenshot placeholder: Schoology submission with class URL and folder path.]

Schoology layouts may differ; follow the instructor's available submission field.
Do not substitute a local computer path or assume pushing to GitHub submits to
Schoology. Keep the instructor as collaborator for feedback.

## If Something Goes Wrong

- Files missing online: confirm you committed, pushed successfully, and refreshed the correct repo.
- App fails after copying: check all required local modules/data are included.
- Git/authentication error: copy the exact message and ask the instructor.
- Pending instructor invitation: verify the username and tell the instructor.
- Never force-push, discard changes, or delete a repository just to clear an error.
