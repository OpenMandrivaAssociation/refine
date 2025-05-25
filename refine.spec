%define _name Refine
%define __name refine
%define rdn_name page.tesk.%_name

Name: refine
Version: 0.5.9
Release: 1
Group:			Graphical desktop/GNOME
Summary: Tweak various aspects of GNOME
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/TheEvilSkeleton/Refine
Source0: https://gitlab.gnome.org/TheEvilSkeleton/Refine/-/archive/%{version}/Refine-%{version}.tar.bz2

BuildRequires: meson 
BuildRequires: pkgconfig(blueprint-compiler)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: desktop-file-utils
BuildRequires: appstream

Requires: python-gobject3
Requires: pyrhon-gi
Requires: typelib(Adw)
Requires: typelib(XdpGtk4) 
Requires: dconf

%description
Refine helps discover advanced and experimental features in GNOME.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson -Dprofile=default
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %__name %rdn_name

%files -f %name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/%__name/
%_iconsdir/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%_iconsdir/hicolor/scalable/apps/%{rdn_name}*.svg
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*
