"""
	DOC: automatically Install Pip Packages With Missing Module && upgrades pip if its old
	# where mode can be {install,uninstall,download} and modules is
	USAGE: require('mode',[modules,...])
	require('install',['pytorch','numpy','etc...'])
	+NOTES: downloading can be useful if want to install later
	from local source and avoid network cost.
	"""
import subprocess as sp
modulesList = [modulesList] if isinstance(
    modulesList, str) else modulesList

proc = sp.run("pip list", stdout=sp.PIPE, stderr=sp.PIPE, text=1)
if "You should consider upgrading" in proc.stderr:
		upgradeCommand = proc.stderr.split("'")
		sp.run(upgradeCommand[1])

	pipInstallSignal, pipUninstallSignal = 0, 0  # declare signals as 0,
	satisfied = {
		x: (x.lower() in proc.stdout.lower()) for x in modulesList
		}  # list booleanization
	for k, v in satisfied.items():
		if not v:
			print(k, "is missing", end=" =|= ")
		# print(k+'\t:preinstalled')  else )
		if v is False:
			pipInstallSignal = 1
		if v is True:
			pipUninstallSignal = 1  # NAND Condition if true then start uninstalling

	if mode == "download":
		proc = sp.run(f'pip download {" ".join(modulesList)} ', stdout=sp.PIPE, shell=0)
		output = proc.stdout.read().decode("ascii").split("\n")
		print([x for x in output if "Successfully" in x][0])
		proc.kill()

	if mode == "install":
		if pipInstallSignal:
			proc = sp.run(
				f'pip install {" ".join(modulesList)} -U'.format(), text=True, shell=1
				)
		else:
			print(f"{modulesList} were already installed")
			return 1

	if mode == "uninstall":
		if pipUninstallSignal:
			proc = sp.run(
				f'pip uninstall -y {" ".join(modulesList)}', text=True, shell=0
				)
		else:
			print(f"\n{modulesList} were already uninstalled")
			return 1

	if proc.returncode == 0:
		print("require Run Success")
		return proc.returncode
