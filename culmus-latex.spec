%define name culmus-latex
%define version 0.5
%define release %mkrel 1

%define texmfdir %{_datadir}/texmf

Summary: Culmus Hebrew fonts for LaTeX
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: Makefile.patch
Patch1: mkCLMtfm.sh.patch
License: GPL
Group: Publishing
Url: http://ivritex.sourceforge.net/
BuildArch: noarch
Requires: fonts-type1-hebrew, tetex
BuildRequires: fonts-type1-hebrew, tetex-afm, tetex
Obsoletes: ivritex

%description
This package provides LaTeX support for the Hebrew fonts distributed by the
Culmus Project.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build

%install
rm -rf $RPM_BUILD_ROOT
%__perl -pi -e 's,/usr/share/texmf,%{buildroot}/usr/share/texmf,' Makefile
%__perl -pi -e 's,/usr/share/fonts/hebrew,/usr/share/fonts/type1/hebrew,' Makefile
make pkginstall

%clean
rm -rf $RPM_BUILD_ROOT

%post
mktexlsr
updmap-sys --enable Map=culmus.map --quiet

%postun
mktexlsr
updmap-sys --disable culmus.map --quiet

%files
%defattr(-,root,root)
%doc README GNU-GPL culmus-ex.tex hebhello.tex
%{texmfdir}/fonts/afm/public/culmus
%{texmfdir}/fonts/type1/public/culmus
%{texmfdir}/fonts/enc/dvips/culmus
%{texmfdir}/fonts/map/dvips/culmus
%{texmfdir}/fonts/tfm/public/culmus
%{texmfdir}/fonts/vf/public/culmus
%{texmfdir}/tex/latex/culmus
%{texmfdir}/tex/generic/0babel
