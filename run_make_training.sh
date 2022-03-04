$path2drive = '/media/yaesop/ARL_FZNV/' ##change this
cd $path2drive
mkdir syn_training/
cd syn_training
mkdir labels
mkdir images
cd ~/SynDataExp ## change this
python make_training_data.py $path2drive
