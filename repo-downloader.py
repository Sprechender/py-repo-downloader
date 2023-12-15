import os
import requests
import questionary
import wget

# clean screen
def clean():
    os.system('cls')

# download release files
def download_assets(releases, username, repo, release_index):
    release = releases[release_index]
    assets = release.get('assets', [])
    
    options = questionary.checkbox(
        f"Select assets to download for Release {release_index + 1}",
        choices=[asset['name'] for asset in assets]
    ).ask()

    for asset in assets:
        clean()

        if asset['name'] in options:
            download_url = asset.get('browser_download_url')
            if download_url:
                filename = download_url.split('/')[-1]
                download_path = f"./{username}/{repo}/"

                os.makedirs(download_path, exist_ok=True)

                print(f"Downloading {filename}...")
                wget.download(download_url, f"{download_path}{filename}")
                print(" <|> Download complete!")

# main
def main():
    ghUsername = questionary.text("Input GitHub Username [https://github.com/...]")
    answer__ghUsername = ghUsername.ask()

    clean()

    ghRepo = questionary.text("Input GitHub Repo-name [https://github.com/"+ answer__ghUsername + "/]")
    answer__ghRepo = ghRepo.ask()

    clean()

    releases_url = f"https://api.github.com/repos/{answer__ghUsername}/{answer__ghRepo}/releases"

    response = requests.get(releases_url)
    if response.status_code == 200:
        releases = response.json()
        release_choices = [f"Release {index + 1}" for index, _ in enumerate(releases)]
        release_index = questionary.select("New -> Old\nSelect a release:", choices=release_choices).ask()

        clean()

        if release_index is not None:
            release_index = int(release_index.split()[1]) - 1
            download_assets(releases, answer__ghUsername, answer__ghRepo, release_index)
    else:
        print("Failed to fetch releases. Please check the repository information.")

# start everything
if __name__ == "__main__":
    main()