%define		debug_package %{nil}

Name:		refine
Version:	0.7.1
Release:	1
Source0:	https://gitlab.gnome.org/TheEvilSkeleton/Refine/-/archive/%{version}/Refine-%{version}.tar.gz
Summary:	Tweak various aspects of GNOME
URL:		https://gitlab.gnome.org/TheEvilSkeleton/Refine
License:	GPL-3.0-or-later
Group:		Graphical desktop/GNOME
BuildRequires:	gettext
BuildRequires:	meson
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:	python-blueprint-compiler
BuildRequires:	appstream

BuildSystem:	meson

%description
This provides a means to tweak various aspects of GNOME

%prep
%autosetup -p1 -n Refine-%{version}

%files -f %name.lang
%{_bindir}/%{name}
%{_datadir}/applications/page.tesk.Refine.desktop
%{_datadir}/dbus-1/services/page.tesk.Refine.service
%{_datadir}/glib-2.0/schemas/page.tesk.Refine.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*Refine*.svg
%{_datadir}/metainfo/page.tesk.Refine.metainfo.xml
%{_datadir}/refine
