%define name	culmus-latex
%define version 0.7
%define release 3

%define texmfdir %{_datadir}/texmf

Summary: 	 Culmus Hebrew fonts for LaTeX
Name: 		 %{name}
Version: 	 %{version}
Release:	1
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


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7-2mdv2011.0
+ Revision: 617477
- the mass rebuild of 2010.0 packages

* Thu Jul 09 2009 Lev Givon <lev@mandriva.org> 0.7-1mdv2010.0
+ Revision: 393909
- Update to 0.7.

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.5-3mdv2009.0
+ Revision: 243805
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.5-1mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Lev Givon <lev@mandriva.org> 0.5-1mdv2008.0
+ Revision: 91152
- Import culmus-latex



* Tue Sep 18 2007 Lev Givon <lev@mandriva.org> 0.5-1mdv2007.1
- Initial Mandriva package.
