%define	name	glui
%define	major	2
%define	minor	2
%define	version	%{major}.36
%define	rel	2

%define libname		%mklibname %{name} %major
%define libnamedev 	%mklibname %{name} %major -d


Summary:	GL User Interface Library
Name:		%name
Version:	2.36
Release:	%mkrel %rel
Group:		System/Libraries
URL:		http://glui.sourceforge.net/
Source:		%{name}-%version.tar.bz2
#patch sent upstream by Kharec
Patch:		glui-2.36-fix-cpp-examples.patch
License:	LGPL
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	libmesaglu-devel libmesaglut-devel

%description
GLUI is a GLUT-based C++ user interface library which provides
controls such as buttons, checkboxes, radio buttons, and spinners
to OpenGL applications. It is window-system independent, relying
on GLUT to handle all system-dependent issues, such as window and
mouse management.

%package -n %libnamedev
Summary: GLUI User Interface Library Development Files
Group: System/Libraries

%description -n %libnamedev
GLUI is a GLUT-based C++ user interface library which provides
controls such as buttons, checkboxes, radio buttons, and spinners
to OpenGL applications. It is window-system independent, relying
on GLUT to handle all system-dependent issues, such as window and
mouse management.
This package includes the header files and static library.

%package -n %name-demos
Summary: GLUI Demos
Group: Graphics

%description -n %name-demos
GLUI is a GLUT-based C++ user interface library which provides
controls such as buttons, checkboxes, radio buttons, and spinners
to OpenGL applications. It is window-system independent, relying
on GLUT to handle all system-dependent issues, such as window and
mouse management.
This package includes some binaries statically built with GLUI.
Their source code is in %_datadir/%name-demos.

%prep
%setup -q 
%patch -p0

%build
mkdir lib
mkdir bin
cd src/
make GLUT_LIB_LOCATION=%{_libdir} GLUT_INC_LOCATION=%{_includedir}/GL CFLAGS="%{optflags}" CC=g++

for i in 1 2 3 4 5; do mv bin/example$i bin/GLUI-example$i; done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
mkdir -p $RPM_BUILD_ROOT%{_includedir}/GL
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT/%_datadir/%name-demos
cp src/lib/*.a $RPM_BUILD_ROOT%{_libdir}
cp src/include/GL/*.h $RPM_BUILD_ROOT%{_includedir}/GL
cp src/bin/* $RPM_BUILD_ROOT/%_bindir
cp src/example/example*.cpp $RPM_BUILD_ROOT/%_datadir/%name-demos

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libnamedev
%defattr(-,root,root)
%doc src/doc/*
%{_includedir}/GL
%{_libdir}/*.a

%files -n %name-demos
%defattr(-,root,root)
%_datadir/%name-demos/example*.cpp
%_bindir/example6
%_bindir/ppm2array
%_bindir/GLUI-example1
%_bindir/GLUI-example2
%_bindir/GLUI-example3
%_bindir/GLUI-example4
%_bindir/GLUI-example5

