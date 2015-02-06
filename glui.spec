%define	major	2

%define libname		%mklibname %{name} %{major}
%define libnamedev 	%mklibname %{name} %{major} -d

Summary:	GL User Interface Library
Name:		glui
Version:	2.36
Release:	4
Group:		System/Libraries
License:	LGPL
URL:		http://glui.sourceforge.net/
Source:		%{name}-%{version}.tar.bz2
#patch sent upstream by Kharec
Patch:		glui-2.36-fix-cpp-examples.patch
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(xmu)


%description
GLUI is a GLUT-based C++ user interface library which provides
controls such as buttons, checkboxes, radio buttons, and spinners
to OpenGL applications. It is window-system independent, relying
on GLUT to handle all system-dependent issues, such as window and
mouse management.

%package -n %{libnamedev}
Summary:	GLUI User Interface Library Development Files
Group:		System/Libraries

%description -n %{libnamedev}
GLUI is a GLUT-based C++ user interface library which provides
controls such as buttons, checkboxes, radio buttons, and spinners
to OpenGL applications. It is window-system independent, relying
on GLUT to handle all system-dependent issues, such as window and
mouse management.
This package includes the header files and static library.

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
%setup -q 
%patch -p0

%build
mkdir lib
mkdir bin
cd src/
make GLUT_LIB_LOCATION=%{_libdir} GLUT_INC_LOCATION=%{_includedir}/GL CFLAGS="%{optflags}" CC=g++

for i in 1 2 3 4 5; do mv bin/example$i bin/GLUI-example$i; done

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_includedir}/GL
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/%{name}-demos
cp src/lib/*.a %{buildroot}%{_libdir}
cp src/include/GL/*.h %{buildroot}%{_includedir}/GL
cp src/bin/* %{buildroot}%{_bindir}
cp src/example/example*.cpp %{buildroot}%{_datadir}/%{name}-demos

%files -n %{libnamedev}
%doc src/doc/*
%{_includedir}/GL
%{_libdir}/*.a

%files -n %{name}-demos
%{_datadir}/%{name}-demos/example*.cpp
%{_bindir}/example6
%{_bindir}/ppm2array
%{_bindir}/GLUI-example1
%{_bindir}/GLUI-example2
%{_bindir}/GLUI-example3
%{_bindir}/GLUI-example4
%{_bindir}/GLUI-example5

%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.36-2mdv2011.0
+ Revision: 610866
- rebuild

* Sun Mar 21 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.36-1mdv2010.1
+ Revision: 526204
- fix Source and %%prep
- rediff patch, partially applied
- fix %%build, %%install, %%files, and %%clean
- patch resent upstream, add a comment
- update to 2.36

* Fri Feb 19 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.35-8mdv2010.1
+ Revision: 507981
- fix URL

* Wed Feb 17 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.35-7mdv2010.1
+ Revision: 506915
- Fix space and tabs for fix rpmlint warning

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.35-6mdv2010.0
+ Revision: 429216
- rebuild

* Fri Sep 19 2008 Funda Wang <fwang@mandriva.org> 2.35-5mdv2009.0
+ Revision: 285799
- fix rel

* Fri Sep 19 2008 Funda Wang <fwang@mandriva.org> 2.35-4mdv2009.0mdv2009.0
+ Revision: 285798
- bump rel
- bunzip the patch
- install to /usr

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.35-3mdv2009.0mdv2009.0
+ Revision: 246253
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.35-1mdv2008.1mdv2008.1
+ Revision: 136445
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import glui


* Fri Dec 23 2005 Anssi Hannula <anssi@mandriva.org> 2.2-6mdk
- fix description
- %%mkrel
- fix library dir for lib64
- quiet %%setup

* Wed Jul 06 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.2-5mdk
- rebuild

* Fri Jun 11 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.2-4mdk
- rebuild

* Thu Mar 6 2003 Austin Acton <aacton@yorku.ca> 2.2-3mdk
- fix library location

* Thu Jan 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.2-2mdk
- rebuild

* Mon Nov 25 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.2-1mdk
- from Austin Acton <aacton@yorku.ca> :
	- initial package for Mandrake 9.0
	- made patch to avoid void main() definitions
