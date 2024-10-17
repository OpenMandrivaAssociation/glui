%define	major	2

%define libname		%mklibname %{name} %{major}
%define oldlibnamedev 	%mklibname %{name} %{major} -d
%define libnamedev 	%mklibname %{name} -d
%define staticname	%mklibname %{name} -d -s

Summary:	GL User Interface Library
Name:		glui
Version:	2.37
Release:	2
Group:		System/Libraries
License:	LGPL
URL:		https://github.com/libglui/glui
Source:		https://github.com/libglui/glui/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		glui-2.37-fix-build-system.patch
Patch1:		glui-2.37-fix-bogus-header.patch
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	cmake ninja

%description
GLUI is a GLUT-based C++ user interface library which provides
controls such as buttons, checkboxes, radio buttons, and spinners
to OpenGL applications. It is window-system independent, relying
on GLUT to handle all system-dependent issues, such as window and
mouse management.

%package -n %{libname}
Summary:	The GL User Interface Library
Group:		System/Libraries

%description -n %{libname}
GLUI is a GLUT-based C++ user interface library which provides
controls such as buttons, checkboxes, radio buttons, and spinners
to OpenGL applications. It is window-system independent, relying
on GLUT to handle all system-dependent issues, such as window and
mouse management.

%package -n %{libnamedev}
Summary:	GLUI User Interface Library Development Files
Group:		Development/C++ and C
Requires:	%{libname} = %{EVRD}
%rename %{oldlibnamedev}

%description -n %{libnamedev}
GLUI is a GLUT-based C++ user interface library which provides
controls such as buttons, checkboxes, radio buttons, and spinners
to OpenGL applications. It is window-system independent, relying
on GLUT to handle all system-dependent issues, such as window and
mouse management.
This package includes the header files.

%package -n %{staticname}
Summary:	GLUI User Interface Library Development Files
Group:		Development/C++ and C
Requires:	%{libnamedev} = %{EVRD}

%description -n %{staticname}
GLUI is a GLUT-based C++ user interface library which provides
controls such as buttons, checkboxes, radio buttons, and spinners
to OpenGL applications. It is window-system independent, relying
on GLUT to handle all system-dependent issues, such as window and
mouse management.
This package includes the static library.

%package -n %{name}-demos
Summary:	GLUI Demos
Group:		Graphics

%description -n %{name}-demos
GLUI is a GLUT-based C++ user interface library which provides
controls such as buttons, checkboxes, radio buttons, and spinners
to OpenGL applications. It is window-system independent, relying
on GLUT to handle all system-dependent issues, such as window and
mouse management.
This package includes some binaries statically built with GLUI.
Their source code is in %{_datadir}/%{name}-demos.

%prep
%autosetup -p1
# What the ****?
find . -name "*.cpp" -o -name "*.h" -o -name "*.c" -o -name "*.ppm" |xargs chmod -x

%cmake -G Ninja

%build
%ninja_build -C build

for i in `seq 1 6`; do
	mv build/example$i GLUI-example$i
done

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_includedir}/GL
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/%{name}-demos
cp build/libglui_static.a %{buildroot}%{_libdir}/libglui.a
cp -a build/*.so* %{buildroot}%{_libdir}/
cp include/GL/*.h %{buildroot}%{_includedir}/GL
cp build/ppm2array *example? %{buildroot}%{_bindir}
cp example/example*.cpp %{buildroot}%{_datadir}/%{name}-demos

%files -n %{libname}
%{_libdir}/libglui.so.%{major}*

%files -n %{libnamedev}
%doc doc/*
%{_includedir}/GL/*
%{_libdir}/*.so

%files -n %{staticname}
%{_libdir}/*.a

%files -n %{name}-demos
%{_datadir}/%{name}-demos/example*.cpp
%{_bindir}/ppm2array
%{_bindir}/GLUI-example1
%{_bindir}/GLUI-example2
%{_bindir}/GLUI-example3
%{_bindir}/GLUI-example4
%{_bindir}/GLUI-example5
%{_bindir}/GLUI-example6
