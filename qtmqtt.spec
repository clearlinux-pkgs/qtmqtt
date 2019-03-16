#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtmqtt
Version  : 5.12.2
Release  : 3
URL      : https://github.com/qt/qtmqtt/archive/v5.12.2/qtmqtt-everywhere-src-5.12.2.tar.gz
Source0  : https://github.com/qt/qtmqtt/archive/v5.12.2/qtmqtt-everywhere-src-5.12.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: qtmqtt-lib = %{version}-%{release}
Requires: qtmqtt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5WebSockets)
BuildRequires : pkgconfig(Qt5Widgets)

%description
The tests included in the subdirectories check for functionality and
conformance of the Qt MQTT module.

%package dev
Summary: dev components for the qtmqtt package.
Group: Development
Requires: qtmqtt-lib = %{version}-%{release}
Provides: qtmqtt-devel = %{version}-%{release}

%description dev
dev components for the qtmqtt package.


%package lib
Summary: lib components for the qtmqtt package.
Group: Libraries
Requires: qtmqtt-license = %{version}-%{release}

%description lib
lib components for the qtmqtt package.


%package license
Summary: license components for the qtmqtt package.
Group: Default

%description license
license components for the qtmqtt package.


%prep
%setup -q -n qtmqtt-5.12.2

%build
## build_prepend content
touch .git
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1552701337
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtmqtt
cp LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtmqtt/LICENSE.GPL3
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtmqtt/LICENSE.GPL3-EXCEPT
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtMqtt/5.12.2/QtMqtt/private/qmqttclient_p.h
/usr/include/qt5/QtMqtt/5.12.2/QtMqtt/private/qmqttconnection_p.h
/usr/include/qt5/QtMqtt/5.12.2/QtMqtt/private/qmqttconnectionproperties_p.h
/usr/include/qt5/QtMqtt/5.12.2/QtMqtt/private/qmqttcontrolpacket_p.h
/usr/include/qt5/QtMqtt/5.12.2/QtMqtt/private/qmqttmessage_p.h
/usr/include/qt5/QtMqtt/5.12.2/QtMqtt/private/qmqttpublishproperties_p.h
/usr/include/qt5/QtMqtt/5.12.2/QtMqtt/private/qmqttsubscription_p.h
/usr/include/qt5/QtMqtt/QMqttAuthenticationProperties
/usr/include/qt5/QtMqtt/QMqttClient
/usr/include/qt5/QtMqtt/QMqttConnectionProperties
/usr/include/qt5/QtMqtt/QMqttLastWillProperties
/usr/include/qt5/QtMqtt/QMqttMessage
/usr/include/qt5/QtMqtt/QMqttMessageStatusProperties
/usr/include/qt5/QtMqtt/QMqttPublishProperties
/usr/include/qt5/QtMqtt/QMqttServerConnectionProperties
/usr/include/qt5/QtMqtt/QMqttStringPair
/usr/include/qt5/QtMqtt/QMqttSubscription
/usr/include/qt5/QtMqtt/QMqttSubscriptionProperties
/usr/include/qt5/QtMqtt/QMqttTopicFilter
/usr/include/qt5/QtMqtt/QMqttTopicName
/usr/include/qt5/QtMqtt/QMqttUnsubscriptionProperties
/usr/include/qt5/QtMqtt/QMqttUserProperties
/usr/include/qt5/QtMqtt/QtMqtt
/usr/include/qt5/QtMqtt/QtMqttDepends
/usr/include/qt5/QtMqtt/QtMqttVersion
/usr/include/qt5/QtMqtt/qmqttauthenticationproperties.h
/usr/include/qt5/QtMqtt/qmqttclient.h
/usr/include/qt5/QtMqtt/qmqttconnectionproperties.h
/usr/include/qt5/QtMqtt/qmqttglobal.h
/usr/include/qt5/QtMqtt/qmqttmessage.h
/usr/include/qt5/QtMqtt/qmqttpublishproperties.h
/usr/include/qt5/QtMqtt/qmqttsubscription.h
/usr/include/qt5/QtMqtt/qmqttsubscriptionproperties.h
/usr/include/qt5/QtMqtt/qmqtttopicfilter.h
/usr/include/qt5/QtMqtt/qmqtttopicname.h
/usr/include/qt5/QtMqtt/qmqtttype.h
/usr/include/qt5/QtMqtt/qtmqttversion.h
/usr/lib64/cmake/Qt5Mqtt/Qt5MqttConfig.cmake
/usr/lib64/cmake/Qt5Mqtt/Qt5MqttConfigVersion.cmake
/usr/lib64/libQt5Mqtt.prl
/usr/lib64/libQt5Mqtt.so
/usr/lib64/pkgconfig/Qt5Mqtt.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_mqtt.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_mqtt_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Mqtt.so.5
/usr/lib64/libQt5Mqtt.so.5.12
/usr/lib64/libQt5Mqtt.so.5.12.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtmqtt/LICENSE.GPL3
/usr/share/package-licenses/qtmqtt/LICENSE.GPL3-EXCEPT
