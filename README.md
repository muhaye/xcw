# xcwsbuild
A xcode's workspace buillder 

## Why using xcwsbuild
This command will allow to build the current dir's xcode workspace using the default scheme
in one easy one word command. This will prevent from using a complexe multiword commmand when
a quick build is all that is needed

```
$ xcwsbuild
```
## Installation procedure

#### 1. Download the script:
```
cd ~/Downloads
```
```
curl -O https://raw.githubusercontent.com/muhaye/xcw/master/xcw.py
```

## Configuration

### 3. Make the script executable
```
chmod u+x xcw.py
```
### 4. Copy the script to exetable path
```
cp xcw.py /usr/local/bin/xcwsbuild
```

## Usage
```
cd /path/to/xcodeproject
xcwsbuild
```
