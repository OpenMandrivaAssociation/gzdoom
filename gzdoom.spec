%define _disable_lto 1
Summary:	Enhanced Doom engine
Name:		gzdoom
Version:	4.2.4
Release:	%mkrel 1
License:	GPLv3+
Group:		Games/Arcade
Url:		https://zdoom.org
Source0:	https://github.com/coelckers/gzdoom/archive/g%{version}.zip

BuildRequires:	cmake
BuildRequires:	imagemagick
BuildRequires:	bzip2-devel
BuildRequires:	libgomp-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(zlib)
Requires:	TiMidity++

Recommends:	doom-iwad
Provides:	doom-engine

Obsoletes:	prboom-plus <= 2.5.4.1
Exclusivearch:	x86_64

%description
GZDoom is a Doom source port based on ZDoom. It features an
OpenGL 4.5 renderer and lots of new features, among them:
- 3D floors
- Dynamic lights
- Quake2/Unreal style skyboxes
- True color texture support
- Model support (limited at the moment)

Warning! Make sure to place WAD files to %{_datadir}/doom/

%files
%{_bindir}/%{name}
%{_gamesdatadir}/doom/brightmaps.pk3
%{_gamesdatadir}/doom/game_support.pk3
%{_gamesdatadir}/doom/gzdoom.pk3
%{_gamesdatadir}/doom/lights.pk3
%{_datadir}/doc/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-g%{version}

sed -i s,"<unknown version>","%{version}",g tools/updaterevision/updaterevision.c

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DINSTALL_PK3_PATH=%{_gamesdatadir}/doom/
%make_build

%install
%make_install -C build

# install menu entry
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=GZDoom
Comment=Enhanced Doom engine
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF


