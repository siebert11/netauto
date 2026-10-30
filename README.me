# Netauto

A Python script that automates config backups with change detection, to reduce the amount of work and time required
to manually maintain and backup several network devices in several locations while working in a multi-branch clinic.

## Installation

### Windows

#### Windows (Command Prompt)

```bat
python -m venv .venv

.venv\Scripts\activate.bat
```

#### Windows (PowerShell)

```powershell
python -m venv .venv

.venv\Scripts\Activate.ps1
```

### macOS and Linux(Bash/Zsh)

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### requirements.txt

```bash
pip install -r requirements.txt
```

## ## Start the test device

a Linux container with an SSH server that stands in for a network device.

prerequisite: Docker Desktop.

```bash
docker build -t fake-switch test-device/
docker run -d -p 2222:22 fake-switch
```

## Configuration

note: the credentials shown below are for the test container.

#### Windows (Command Prompt)

```bat
set NET_USER=netadmin
set NET_PASSWORD=netadmin123
```

#### Windows (PowerShell)

```powershell
$env:NET_USER="netadmin"
$env:NET_PASSWORD="netadmin123"
```

### macOS and Linux(Bash/Zsh)

```bash
export NET_USER=netadmin
export NET_PASSWORD=netadmin123
```

note: due to currently the container being tested is a Linux image, we will need to invoke the changes ourselves.
the following command will change the text in the config file to test the script capability of recodeing changes.

```bash
docker exec <container-name> sh -c "echo 'hostname sw2' > /home/netadmin/config.txt"
```

## Usage

note: run it from the project folder.

### Windows(Cmd/PowerShell)

```powershell
python backup_config.py
```

### macOS and Linux(Bash/Zsh)

```bash
python3 backup_config.py
```
## Example output

+++ and --- represents the backup files that are being compared, while - and + shows changes in specific line.

```diff
--- backup_2026-10-29_09-13-27.txt
+++ backup_2026-10-29_09-14-25.txt
@@ -1 +1 @@
-hostname sw1
+hostname sw2
```

## Limitations

- Currently tested against a Linux container; Cisco IOS support planned.
- Right now the host, port and device type are hardcoded in the script.
- Untested on Windows; PowerShell may block activation `Activate.ps1`.