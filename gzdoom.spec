#global build_ldflags %{build_ldflags} -Wl,--undefined-version
%define _disable_lto 1
%define _disable_ld_no_undefined 1

%undefine _debugsource_packages

Summary:	Enhanced Doom engine
Name:		gzdoom
Version:	4.12.2
Release:	1
License:	GPLv3+
Group:		Games/Arcade
Url:		https://zdoom.org
Source0:	https://github.com/coelckers/gzdoom/archive/g%{version}/%{name}-g%{version}.zip
#Patch0:		gzdoom-discord.patch
#Patch1:		gzdoom-4.10.0-compile.patch

BuildRequires:	cmake
BuildRequires:	imagemagick
BuildRequires:	bzip2-devel
BuildRequires:	libgomp-devel
BuildRequires:	jpeg-devel
BuildRequires:	discord-rpc-devel
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(vpx)
BuildRequires:  cmake(ZMusic)
Requires:       zmusic
Requires:	TiMidity++
Requires:	discord-rpc

Recommends:	doom-iwad
Provides:	doom-engine

Obsoletes:	prboom-plus <= 2.5.4.1

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
#{_libdir}/libdiscord-rpc.so
%{_gamesdatadir}/doom/brightmaps.pk3
%{_gamesdatadir}/doom/game_support.pk3
%{_gamesdatadir}/doom/gzdoom.pk3
%{_gamesdatadir}/doom/lights.pk3
%{_gamesdatadir}/doom/fm_banks/
%{_gamesdatadir}/doom/game_widescreen_gfx.pk3
%{_gamesdatadir}/doom/soundfonts/gzdoom.sf2
%{_datadir}/doc/%{name}/
%{_datadir}/applications/%{name}.desktop
#{_iconsdir}/hicolor/*/apps/%{name}.png
#{_includedir}/discord*

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-g%{version}
%autopatch -p1

#sed -i s,"<unknown version>","%{version}",g tools/updaterevision/updaterevision.c

%build
#export CC=gcc
#export CXX=g++
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
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


