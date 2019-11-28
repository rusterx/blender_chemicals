# blender_chemicals
blender_chemicals is a blender addon based on blender-chemicals[^1] which is used to render smile string to molecule structure based on chemical-structures. Because the python api of latest version (2.80+) blender have some difference with previous version. Therefore, we correct the unproper code of blender-chemicals and change it to an blender addon.

![Screenshot of addon](./images/blender_chemicals_screenshot.jpg)

Install support software
---
This blender addon is based on the function of simle string to json format atom and bond location structure from openbabel. Therefore, the installation of openbabel is necessary. However, the installation is very tough and the below guide is recommended. 

* Install conda command from Anaconda[^2]
* Install openbabel using conda command
```bash
conda install -c openbabel openbabel
```

You can test the openbabel installation by import bypel and openbabel package in python environment.

Install Blender_Chemicals
---
- Download this repo of the blender_chemicals and compress it as a zip file.
- Load the zip file as an addon in blender [Edit]-[Preferences]-[Addon] as below.

![Install Addon](./images/install_addon.jpg)

- Press <kbd>N</kbd> key to display properties panel and just use it.

[^1]: <https://github.com/patrickfuller/blender-chemicals>
[^2]: <https://conda.io/projects/conda/en/latest/user-guide/install/windows.html>