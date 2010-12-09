%define name	culmus-latex
%define version 0.7
%define release %mkrel 2

%define texmfdir %{_datadir}/texmf

Summary: 	 Culmus Hebrew fonts for LaTeX
Name: 		 %{name}
Version: 	 %{version}
Release: 	 %{release}
Source0: 	 %{name}-%{version}-r1.tar.gz
Patch0: 	 Makefile.patch
License: 	 GPLv2
Group: 		 Publishing
Url: 		 http://ivritex.sourceforge.net/
BuildRoot: 	 %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	 noarch
Requires: 	 fonts-type1-hebrew, tetex
BuildRequires: 	 fonts-type1-hebrew, tetex-afm, tetex
Obsoletes: 	 ivritex

%description
This package provides LaTeX support for the Hebrew fonts distributed by the
Culmus Project.

%prep
%setup -q -n %{name}-%{version}-r1
%patch0 -p0

%install
%__rm -rf %{buildroot}
make DESTDIR=%{buildroot} pkginstall

%clean
%__rm -rf %{buildroot}

%post
mktexlsr
updmap-sys --enable Map=culmus.map --quiet

%postun
mktexlsr
updmap-sys --disable culmus.map --quiet

%files
%defattr(-,root,root)
%doc README GNU-GPL LICENSE-Culmus examples/
%{texmfdir}/fonts/afm/public/culmus
%{texmfdir}/fonts/type1/public/culmus
%{texmfdir}/fonts/enc/dvips/culmus
%{texmfdir}/fonts/map/dvips/culmus.map
%{texmfdir}/fonts/tfm/public/culmus
%{texmfdir}/fonts/vf/public/culmus
%{texmfdir}/tex/latex/culmus
%{texmfdir}/tex/generic/0babel
