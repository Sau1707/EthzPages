# EthzPages

A python scraper for the student websites of ethz

## Setup

Create python enviroment

```
python -m venv venv
```

## Get usernames

In order to make the scraper works, we need to collect the list of usernames of all the students, to do that, create a network folder with this location

```
\\d.ethz.ch\users\all
```

Then open a terminal in that location and run the follow:

```
Get-ChildItem -Path .\ -Directory | Select-Object -ExpandProperty Name | Set-Content -Path "$([Environment]::GetFolderPath('Desktop'))\ethz_names.txt"
```

If will create a file called `ethz_names.txt` with all the usernames on the desktop, there are around 55'000 folder it will take a few seconds.
