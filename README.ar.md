<p align="center">
  <a href="./README.md">
    <img src="https://img.shields.io/badge/-EN-000000?style=social&logo=googletranslate&logoColor=white" alt="EN" height="18">
  </a>
  <a href="./README.ar.md">
    <img src="https://img.shields.io/badge/-AR-000000?style=social&logo=googletranslate&logoColor=white" alt="AR" height="18">
  </a>
  <a href="./README.fr.md">
    <img src="https://img.shields.io/badge/-FR-000000?style=social&logo=googletranslate&logoColor=white" alt="FR" height="18">
  </a>
</p>

# برمجة الروبوتات — DSAI 4304

ملاحظاتي وتلخيصاتي ولاباتي وكود ROS 2 الخاص بي لمساق
**برمجة الروبوتات (DSAI 4304)** في الكلية الجامعية للعلوم التطبيقية.

**المدرّسة:** د. شادية بارود  
**الفصل:** الفصل الأول، 2026–2007  
**البيئة:** Ubuntu 24.04 · ROS 2 Jazzy · Gazebo Harmonic · RViz2

---

## ما يوجد في هذا الريبو

| المجلد | المحتوى |
|---|---|
| `docs/syllabus.md` | نسخة Markdown من السيلابس |
| `docs/schedule.md` | الخطة الأسبوعية (14 أسبوعًا) |
| `docs/weeks/week01…week14/` | مفاهيم أسبوعية وتلخيصاتي وملاحظات اللاب |
| `docs/notes/` | أوراق مرجعية ومعجم ومراجعة امتحانات |
| `ros2_ws/src/` | حزم ROS 2 التي أبنيها في اللابات |
| `simulations/` | عوالم Gazebo وملفات RViz و ROS bags |
| `templates/` | قوالب تقارير اللاب والتلخيص |

---

## لماذا أحتفظ بهذا الريبو

أستخدم هذا الريبو لجمع عمل المساق في مكان واحد:
المفاهيم التي أقرأها، التلخيصات بكلماتي، اللابات التي أنفذها،
والكود الذي أكتبه. هذا يسهّل المراجعة ويسمح لي بالعودة إلى أي أسبوع
دون البحث في نظام إدارة التعلم (LMS).

---

## ملاحظة تحفيزية صغيرة

تابعت مؤتمر **IROS 2026** (IEEE/RSJ International Conference on Intelligent
Robots and Systems) افتراضيًا في نوفمبر 2026. رؤية الأعمال الحالية حول
نماذج Vision-Language-Action والحساسية اللمسية والتحكم القائم على التعلم
جعلت المساق يبدو كنقطة انطلاق وليس مجرد تمارين.
لا تزال بيانات الروبوتات الواقعية أكبر عقبة — لا تستطيع الروبوتات الاعتماد
على نصوص الإنترنت بحجم ما تعتمد عليه النماذج اللغوية — وهذا جزء من سبب
أهمية لابات المحاكاة.

هذا الريبو سجلي لهذا العمل.

---

## دليل الإعداد: ROS 2 على Ubuntu عبر VirtualBox

هذا الدليل يشرح تثبيت **ROS 2** داخل بيئة Ubuntu على جهاز افتراضي
VirtualBox لتطوير الروبوتات.

### الخطوة 1 — إعداد Ubuntu في VirtualBox

1. **تحميل البرامج المطلوبة:**
   * حمّلي وثبّتي [VirtualBox](https://virtualbox.org).
   * حمّلي **Ubuntu Desktop ISO** الرسمي (استخدمي **24.04 LTS** لـ
     ROS 2 Jazzy، أو **22.04 LTS** لـ ROS 2 Humble).
2. **إنشاء الجهاز الافتراضي:**
   * افتحي VirtualBox، اضغطي **New**، واختاري ملف ISO.
3. **تخصيص الموارد:**
   * **RAM:** 4 GB حد أدنى (يُفضّل 8 GB).
   * **CPU:** من 2 إلى 4 أنوية.
   * **القرص:** 35–50 GB حد أدنى (أدوات المحاكاة تستهلك مساحة كبيرة).
4. **تثبيت Ubuntu:** شغّلي الجهاز، أكملي التثبيت، وافتحي Terminal
   (`Ctrl` + `Alt` + `T`).

### الخطوة 2 — تثبيت ROS 2 (بيئة سطح المكتب)

نفّذي الأوامر التالية في Terminal.

#### 2.1 إعداد اللغة والمستودعات

```bash
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

sudo apt install software-properties-common
sudo add-apt-repository universe
```

2.2 إضافة مفتاح ROS 2

```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg
```

2.3 إضافة قائمة المستودعات

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" \
| sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

2.4 تثبيت حزم ROS 2

```bash
sudo apt update && sudo apt upgrade -y
```

اختاري واحدة فقط حسب إصدار Ubuntu:

· Ubuntu 24.04 (ROS 2 Jazzy):
  ```bash
  sudo apt install ros-jazzy-desktop
  ```
· Ubuntu 22.04 (ROS 2 Humble):
  ```bash
  sudo apt install ros-humble-desktop
  ```

الخطوة 3 — إعداد متغيرات البيئة

لتشغيل سكربت ROS 2 تلقائيًا مع كل نافذة Terminal جديدة:

· ROS 2 Jazzy:
  ```bash
  echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
  source ~/.bashrc
  ```
· ROS 2 Humble:
  ```bash
  echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
  source ~/.bashrc
  ```

الخطوة 4 — التحقق من التثبيت

للتأكد من أن عقد ROS 2 تتواصل:

1. في نافذة Terminal، شغّلي Talker بلغة C++:
   ```bash
   ros2 run demo_nodes_cpp talker
   ```
2. في نافذة ثانية (Ctrl + Shift + T)، شغّلي Listener بلغة Python:
   ```bash
   ros2 run demo_nodes_py listener
   ```

إعدادات VirtualBox المهمة للروبوتات

محاكيات مثل Gazebo تحتاج تسريعًا رسوميًا. عدّلي هذه الإعدادات
والجهاز مُطفأ:

· Settings → Display.
· ارفعي Video Memory للحد الأقصى (128 MB أو 256 MB).
· فعّلي 3D Acceleration. هذا يمنع تعليق RViz و Gazebo أو انهيار الرسوميات.

---

الترخيص

· الكود: MIT
· الملاحظات والتلخيصات: CC BY-NC-SA 4.0

