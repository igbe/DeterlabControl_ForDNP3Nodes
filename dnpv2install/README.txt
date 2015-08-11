This folder hold files that is used to install dnp3v2 on Ubuntu nodes which is housed in DETERLAB.
Hence, trying to run this code oustside deterlab would require modifications.
to run this file in DeterLab iterate through the following steps:

1.  log into deter users.isi.deterlab.net via ssh by running
    
    ssh yourusername@users.isi.deterlab.net
    
    this will bring you into the users network were your files are accessible.

2.  Clone this repository by running
    
    git clone https://gitlab.com/obiigbe91/DeterlabControl.git
    
    supply obiigbe91's username and password. This will download a copy of the repo (DeterlabControl) to your system 

3.  cd DeterlabControl/dnpv2install
4.  bash main.sh
    this should install dnpv2 on all your nodes
    
    
    NOTE--------->use main1.sh for step 4 until main.sh is corrected.<-----NOTE
    
    TODO--correction:
    
    
    read line not working (main.sh)..it runs for only the first node in the attack list, then terminates.
    while read line; do
    node_install $line
    echo "done with second"
done < /tmp/nodelist.txt