<p align="center">
  <kbd>EN</kbd> <a href="./README.ar.md"><kbd>ع</kbd></a> <a href="./README.fr.md"><kbd>FR</kbd></a>
</p>

# Programmation Robotique — DSAI 4304

Mes notes personnelles, résumés, travaux pratiques et code ROS 2 pour
**Programmation Robotique (DSAI 4304)** à l'University College of Applied Sciences.

**Enseignante :** Dr. Shadia Baroud  
**Trimestre :** Premier semestre, 2026–2007  
**Environnement :** Ubuntu 24.04 · ROS 2 Jazzy · Gazebo Harmonic · RViz2

---

## Contenu du dépôt

| Dossier | Contenu |
|---|---|
| `docs/syllabus.md` | Syllabus du cours (copie Markdown) |
| `docs/schedule.md` | Plan sur 14 semaines |
| `docs/weeks/week01…week14/` | Concepts hebdomadaires, mes résumés, notes de TP |
| `docs/notes/` | Fiches mémo, glossaire, révision d'examens |
| `ros2_ws/src/` | Paquets ROS 2 créés pendant les TP |
| `simulations/` | Mondes Gazebo, configs RViz, ROS bags |
| `templates/` | Modèles de rapport de TP et de résumé |

---

## Pourquoi je tiens ce dépôt

Je regroupe ici tout le travail du cours au même endroit :
les concepts lus, mes résumés avec mes propres mots, les TP réalisés
et le code écrit. Cela facilite la révision et me permet de revenir
à n'importe quelle semaine sans chercher dans le LMS.

---

## Petite note de motivation

J'ai suivi **IROS 2026** (IEEE/RSJ International Conference on Intelligent
Robots and Systems) en ligne en novembre 2026. Voir les travaux actuels sur
les modèles Vision-Language-Action, la perception tactile et le contrôle
par apprentissage a transformé ce cours en point de départ plutôt qu'en
simple série d'exercices.
Les données réelles des robots restent le principal goulot d'étranglement —
les robots ne peuvent pas s'appuyer sur du texte à l'échelle d'Internet
comme les modèles de langage — ce qui explique l'importance des TP
basés sur la simulation.

Ce dépôt est ma trace de ce travail.

---

## Guide d'installation : ROS 2 sur Ubuntu via VirtualBox

Ce guide explique comment installer **ROS 2** dans un environnement Ubuntu
hébergé sur une machine virtuelle VirtualBox pour le développement robotique.

### Étape 1 — Configurer Ubuntu dans VirtualBox

1. **Télécharger les logiciels requis :**
   * Téléchargez et installez [VirtualBox](https://virtualbox.org).
   * Téléchargez l'**ISO Ubuntu Desktop** officielle (utilisez **24.04 LTS**
     pour ROS 2 Jazzy, ou **22.04 LTS** pour ROS 2 Humble).
2. **Créer la machine virtuelle (VM) :**
   * Ouvrez VirtualBox, cliquez **New**, et sélectionnez l'ISO téléchargée.
3. **Allouer des ressources adéquates :**
   * **RAM :** 4 Go minimum (8 Go fortement recommandé).
   * **CPU :** 2 à 4 cœurs.
   * **Disque dur :** 35–50 Go minimum (les outils de simulation robotique
     consomment énormément d'espace).
4. **Installer Ubuntu :** démarrez la VM, terminez l'installation standard
   d'Ubuntu, puis ouvrez le Terminal (`Ctrl` + `Alt` + `T`).

### Étape 2 — Installer ROS 2 (environnement bureau)

Exécutez les blocs de commandes suivants dans le Terminal Ubuntu.

#### 2.1 Configurer la locale et les dépôts

```bash
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

sudo apt install software-properties-common
sudo add-apt-repository universe
```

2.2 Ajouter la clé GPG ROS 2

```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg
```

2.3 Ajouter la liste des sources

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" \
| sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

2.4 Installer les paquets ROS 2

```bash
sudo apt update && sudo apt upgrade -y
```

Choisissez une des options ci-dessous selon votre version d'Ubuntu :

· Pour Ubuntu 24.04 (ROS 2 Jazzy) :
  ```bash
  sudo apt install ros-jazzy-desktop
  ```
· Pour Ubuntu 22.04 (ROS 2 Humble) :
  ```bash
  sudo apt install ros-humble-desktop
  ```

Étape 3 — Configurer les variables d'environnement

Automatisez l'exécution du script ROS 2 à chaque nouveau terminal :

· Pour ROS 2 Jazzy :
  ```bash
  echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
  source ~/.bashrc
  ```
· Pour ROS 2 Humble :
  ```bash
  echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
  source ~/.bashrc
  ```

Étape 4 — Vérifier l'installation

Pour vérifier que les nœuds ROS 2 peuvent communiquer dans votre
environnement virtuel :

1. Ouvrez un terminal et lancez le Talker C++ :
   ```bash
   ros2 run demo_nodes_cpp talker
   ```
2. Ouvrez un second terminal (Ctrl + Shift + T) et lancez le
   Listener Python :
   ```bash
   ros2 run demo_nodes_py listener
   ```

Paramètres VirtualBox importants pour la robotique

Les simulateurs physiques comme Gazebo nécessitent une forte
accélération graphique. Réglez ces paramètres VM éteinte :

· Allez dans Settings → Display.
· Poussez le curseur Video Memory au maximum (128 Mo ou 256 Mo).
· Cochez Enable 3D Acceleration. Cela évite que RViz et Gazebo
  ne ralentissent ou ne plantent graphiquement.

---

Licence

· Code : MIT
· Notes et résumés : CC BY-NC-SA 4.0
