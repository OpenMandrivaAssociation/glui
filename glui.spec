%define name glui
%define major 2
%define minor 2
%define version %{major}.35
%define rel 5

%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d


Summary: GL User Interface Library
Name: %name
Version: 2.35
Release: %mkrel %rel
Group: System/Libraries
URL: http://www.cs.unc.edu/~rademach/glui
Source: glui_v%{major}_%{minor}.tar.bz2
Patch: glui.patch
License: LGPL
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: libmesaglu-devel libmesaglut-devel

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
%setup -q -n glui_v%{major}_%{minor}
%patch -p1

%build
mkdir lib
mkdir bin
make GLUT_LIB_LOCATION=%{_libdir} GLUT_INC_LOCATION=%{_includedir}/GL CFLAGS="%{optflags}" CC=g++
for i in 1 2 3 4 5; do mv bin/example$i bin/GLUI-example$i; done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
mkdir -p $RPM_BUILD_ROOT%{_includedir}/GL
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT/%_datadir/%name-demos
cp lib/*.a $RPM_BUILD_ROOT%{_libdir}
cp *.h $RPM_BUILD_ROOT%{_includedir}/GL
cp bin/* $RPM_BUILD_ROOT/%_bindir
cp example*.cpp $RPM_BUILD_ROOT/%_datadir/%name-demos

%clean
rm -r $RPM_BUILD_ROOT

%files -n %libnamedev
%defattr(-,root,root)
%doc glui_manual.pdf readme.txt
%{_includedir}/GL
%{_libdir}/*.a

%files -n %name-demos
%defattr(-,root,root)
%_datadir/%name-demos/example*.cpp
%_bindir/GLUI-example*

