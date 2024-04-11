# Steps to run cuda Quantum docker on CDAC system.
### Step 1:
#### Login into CDAC system:

    $ ssh username@login.npsf.cdac.in
 
     Enter the shared password
     
### Step 2:
  Once logged in, import the latest cuda Quantum version using enroot
  
    $ enroot import docker://nvcr.io#nvidia/nightly/cuda-quantum:latest Step 3: create the sqsh file using
    
    $ enroot create nvidia+nightly+cuda-quantum+latest.sqsh Step 4: Switch to runtime mode using srun
    
    $ srun --partition=bootcp --nodes=1 --ntasks-per-node=256 --time=01-00:00 --gres=gpu:A100-SXM4:8 --pty /bin/bash --env NVIDIA_DISABLE_REQUIRE=1

### Step 5: Starting cuda Quantum

    $ enroot start nvidia+nightly+cuda-quantum+latest.sqsh
    
### Till step 5 it will enable the run of cuda Quantum through the command line. For Jupyter Notebook:

#### Step 6: Set Proxy’s

    $ export http_proxy=http://proxy-10g.10g.siddhi.param:9090
    $ export https_proxy=http://proxy-10g.10g.siddhi.param:9090
    $ export ftp_proxy=http://proxy-10g.10g.siddhi.param:9090
    
#### Step 7: Install Jupyter Notebook using pip 
    $ pip install notebook
    
### Step 7: Launch the jupyter server in the runtime

    $ jupyter notebook --ip=0.0.0.0 --port=9510 --allow-root --no-browser &
    
### Step 8 : Open new terminal on local machine and tunnel

    $ ssh -f -N -L 5665:scn10-10g:9510 user@login.npsf.cdac.in 
    
  `NOTE - One can specify any local port number as Tunnel Port (>1024).
  Since we are getting node 10 , the URL is 5665:scn10-10g:9510 
  If we got Node 16, the URL changes to 5665:scn16-10g:9510`
  
  
### Step 9 : Now, open a web browser on your local system and in a new tab, pass the following link:

    http://localhost:5665

### Step 10: A prompt is shown to enter the token. Use the token value generated in the previous terminal.

Now, you can easily access/open your jupyter notebook
