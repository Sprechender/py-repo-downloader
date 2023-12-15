# GitHub Release Assets Downloader (repo-downloader.py)

Python script that downloads the releases for a specific repository.

## Prerequisites

Before using this script, ensure you have the following installed:

- Python 3.x
- Required Python libraries (`requests`, `questionary`, `wget`). Installable with `requirements.txt` file.

## How to Use

1. Clone the repository or download the Python script.
2. Install the necessary Python libraries if you haven't already:

    ```bash
    pip install -r requirements.txt
    ```
    or
    ```bash
    pip install requests questionary wget
    ```

3. Run the script:

    ```bash
    python repo-downloads.py
    ```

4. Upon execution, the script will prompt for the following information:
    - GitHub Username: Input the GitHub username of the repo-owner (e.g., `https://github.com/obsproject`)
    - GitHub Repo-name: Input the repository name associated with your GitHub account (e.g., `https://github.com/obsproject/obs-studio`)

5. The script will fetch the releases for the provided repository and display them in a list.
6. Select a release (from newest to oldest) that you want to download assets from.
7. Choose the desired assets from the selected release.
8. The assets will be downloaded to a folder named after the GitHub username and repository in the current directory.

## Notes

- Ensure that you everyvidy has the necessary permissions to access the repository's releases and their assets.
- This script relies on the GitHub API. If there are any issues with fetching releases, verify the repository information and your internet connection.
- For any questions, feedback, or issues, feel free to open an issue..