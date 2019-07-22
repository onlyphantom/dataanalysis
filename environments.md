# Python virtual environment for data scientists
## Virtual environments
A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tool for production-level code.

From my own experience, folks from the scientific computing community often dive into the notebook and install packages as we go without necessarily taking time to set up environments. This is dangerous and leads to numerous frustration down the road:
- Having to downgrade / upgrade packages mutiple times as we "switch" projects
- Without isolation of dependencies, this also hurts reproducibility, making it difficult to collaborate on a single project
- Difficult to troubleshoot project errors
- Temptation to stick to legacy packages or Python version as updating one of them may break several projects

If you're doing data science work alone, with no concern on collaboration, and only using your computer to do exactly one project, you'd probably be fine. If your use case of data science falls outside that oddly specific scenario, I strongly recommend you follow this chapter closely.

## Prerequisites
Ananconda / Miniconda: [Installation — Anaconda 2.0 documentation](http://docs.anaconda.com/anaconda/install/)

> Both _Anaconda_ and _Miniconda_ uses Conda as the package manager. The primary difference is the ~720+ packages that are bundled into _Anaconda_ (~3GB of disk space). 
> If you want a lightweight version that includes only _conda_, its dependencies, and Python, use _Miniconda_. 
> 
> Tips: To verify that you have conda installed, open a terminal and run `conda --version`

## Learning Approaches
In the workshop, we will be using the terminal (eg. command line, or bash) to create, manage, and activate our environments. We will also use the terminal to start up a Jupyter notebook / Lab instead of using a Graphical User Interface (GUI) such as the Ananconda Navigator. For this reason it is completely safe to pick either _Anaconda_ or _Miniconda_. 

#### Why CLI over GUI?
Learning how to work in the conda shell and terminal may add some upfront overhead, but they are well worth it in the long run. Being comfortable with the command line interface (CLI) allows you to make the most out of what the development tool has to offer, unrestricted by the implementation choices of a Graphical user interface. 

When you're ready to move your code into production (eg. a virtual machine or an Ubuntu server from Azure), you may have to use SSH (secure shell) or use a Cloud Shell service (such as Azure) to provision, set up, and manage your development services as well as configure environment settings. By learning how to do these work using the command line interface (CLI) now, you will feel right at home later on when there's no GUI to fall back on.

## Creating your virtual environment
To see all conda environments currently installed on your machine, use:
```bash
conda env list

# conda environments:
#
analyst                 /anaconda3/envs/analyst
deeplearning            /anaconda3/envs/deeplearning
microblog               /anaconda3/envs/microblog
networking              /anaconda3/envs/networking
pedagogy                /anaconda3/envs/pedagogy
tokopedia               /anaconda3/envs/tokopedia
root               *    /anaconda3
```
The environment with an asterisk (`*`) next to it indicates the current active environment. 

The following command creates a new environment named `tokopedia` with Python 3 installed.
```bash
mkdir IntroPython
conda create -n tokopedia python=3
source activate tokopedia
```

At the creation stage (`conda create -n`), conda may try to install some packages and prompt for your confirmation:
```
Proceed ([y]/n)? 
```
Type `y` to proceed. When the environment is created, use `source activate <environment name>` to activate the environment.

Run `conda env list` again and you should confirm that you're now using the `tokopedia` environment. 

## Packages in your virtual environment
When you first create your `tokopedia` virtual environment, a number of packages were installed. What are all the packages currently in your environment? What version of each package, respectively, are you using? Conda can list them for us:

```bash
conda list

# packages in environment at /anaconda3/envs/tokopedia:
#
ca-certificates           2019.5.15                     0  
certifi                   2019.6.16                py37_0  
libcxx                    4.0.1                hcfea43d_1  
libcxxabi                 4.0.1                hcfea43d_1  
libedit                   3.1.20181209         hb402a30_0  
libffi                    3.2.1                h475c297_4  
ncurses                   6.1                  h0a44026_1 
...
```

For the Data Analytics Specialization, we will be using `numpy` and `pandas` primarily for most of the classes. If you took the Miniconda option, these are packages that you'll need to install individually.

If `numpy` is not already present, install it using `conda install <package_name>`:

```bash
conda install numpy

Fetching package metadata ...........
Solving package specifications: .

Package plan for installation in environment /anaconda3/envs/tokopedia:

The following NEW packages will be INSTALLED:

    blas:         1.0-mkl              
    intel-openmp: 2019.4-233           
    ...
```

When prompted by `conda`, type `y` to proceed with the installation of `numpy` and its dependencies. 

Now repeat the last step to install `pandas`. 

> You can type the "up-arrow" button in your terminal and this will toggle through your previous commands. This can be a very convenient shortcut instead of typing the full `bash install pandas` command. 

## Packages not in your virtual environment

When you're done installing `numpy` and `pandas`, deactivate your environment and then list all packages again:

```bash
source deactivate
conda list
```
You will notice that conda now return all packages in your root environment, instead of the ones in your `tokopedia` environment. This may mean a different version of Python, a different version of `pandas` and `numpy`. 

## Notebook Kernels 
At this point, you may start up Jupyter Lab and realize that your `tokopedia` environment is not being used. This is because the corresponding package (`notebook`) is installed in your root environment, and has no access to the Python modules in your other environments. 

We can fix this with the use of two additional packages. 

First, in the root environment where you typically launch JupyterLab (or Jupyter Notebook) from, install `nb_conda_kernels`. This is the **environment** that contains the `notebook` package.

```bash
conda install nb_conda_kernels
```

Then, activate your `tokopedia` environment and install the `ipykernel` into this environment.

Alternatively, you can use the `-n` flag and pass in the name of the environment to which a package is installed to.

The `ipykernel` package allow us to create a new kernel with a specified name (by convention, I use the same name as my environment):

```bash
conda install -n tokopedia ipykernel
ipython kernel install --name=tokopedia  

# Success!
Installed kernelspec tokopedia in /usr/local/share/jupyter/kernels/tokopedia
```

When this is done, launch JupyterLab (`jupyter lab`) and you'll see the kernel as an option in your JupyterLab interface. You're all ready to go!

![](/assets/kernels.png)

## Final Words

Congratulations! You've taken the "hard choice" to set up environments for your project. This form of isolation helps you run several projects on your machine, each having its own version of packages and dependencies. Your project collaborators are going to love you for that, and your future self will appreciate you take the extra effort to "do things right" at the beginning.
