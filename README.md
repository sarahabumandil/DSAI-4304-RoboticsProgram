# DSAI-4304-RoboticsProgram

## ROS 2 Setup Guide on Ubuntu via VirtualBox

This guide walks you through installing **ROS 2** inside an Ubuntu Linux environment hosted on a VirtualBox virtual machine for robotics development.

---

## Step 1: Set Up Ubuntu in VirtualBox

1. **Download Required Software:**
   * Download and install [VirtualBox](https://virtualbox.org).
   * Download the official **Ubuntu Desktop ISO** (use **24.04 LTS** for ROS 2 Jazzy, or **22.04 LTS** for ROS 2 Humble).
2. **Create the Virtual Machine (VM):**
   * Open VirtualBox, click **New**, and select your downloaded Ubuntu ISO.
3. **Allocate Adequate Resources:**
   * **RAM:** Minimum **4 GB** (8 GB highly recommended).
   * **CPU:** **2 to 4 cores**.
   * **Hard Disk:** Minimum **35–50 GB** (Robotics simulation tools consume massive storage space).
4. **Install Ubuntu:** Start the VM, complete the standard Ubuntu installation, and open your Terminal (`Ctrl` + `Alt` + `T`).

---

## Step 2: Install ROS 2 (Desktop Environment)

Open your Ubuntu terminal and execute the following blocks of commands.

### 1. Set up Locale & Repositories
```bash
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

sudo apt install software-properties-common
sudo add-apt-repository universe
```

### 2. Add the ROS 2 GPG Key
```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://githubusercontent.com -o /usr/share/keyrings/ros-archive-keyring.gpg
```

### 3. Add the Sources List
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://ros.org $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

### 4. Install ROS 2 Packages
```bash
sudo apt update && sudo apt upgrade -y
```

Choose **one** of the options below depending on your Ubuntu version:

* **For Ubuntu 24.04 (ROS 2 Jazzy):**
  ```bash
  sudo apt install ros-jazzy-desktop
  ```
* **For Ubuntu 22.04 (ROS 2 Humble):**
  ```bash
  sudo apt install ros-humble-desktop
  ```

---

## Step 3: Configure Environment Variables

Automate the sourcing of the ROS 2 setup script so it runs every time you open a new terminal:

* **For ROS 2 Jazzy:**
  ```bash
  echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
  source ~/.bashrc
  ```
* **For ROS 2 Humble:**
  ```bash
  echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
  source ~/.bashrc
  ```

---

## Step 4: Verify the Installation

To verify that ROS 2 nodes can communicate across your virtual environment:

1. Open a terminal window and launch the C++ **Talker**:
   ```bash
   ros2 run demo_nodes_cpp talker
   ```
2. Open a second, separate terminal window (`Ctrl` + `Shift` + `T`) and launch the Python **Listener**:
   ```bash
   ros2 run demo_nodes_py listener
   ```

---

## Important VirtualBox Settings for Robotics

Physics simulators like **Gazebo** require heavy graphical acceleration. Ensure you adjust these settings while the virtual machine is **powered off**:

* Go to **Settings -> Display**.
* Max out your **Video Memory** slider (to 128MB or 256MB).
* Check the box to **Enable 3D Acceleration**. This keeps environments like RViz and Gazebo from lagging or throwing graphics crashes.
