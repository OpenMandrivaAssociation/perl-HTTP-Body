%define	upstream_name	 HTTP-Body
%define upstream_version 1.19

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:	HTTP Body Parser
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTTP/HTTP-Body-%{upstream_version}.tar.gz

BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(YAML)
BuildRequires:  perl-devel

BuildArch:	    noarch

%description
Perl module to parse HTTP request bodies.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README Changes
%{perl_vendorlib}/HTTP/Body/*
%{perl_vendorlib}/HTTP/Body.pm
%{_mandir}/man3/*


%changelog
* Wed Mar 23 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 648088
- update to new version 1.12
- update to new version 1.11

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-1mdv2011.0
+ Revision: 572221
- update to 1.09

* Mon Jan 25 2010 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2011.0
+ Revision: 495703
- update to 1.07

* Sun Jan 10 2010 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.1
+ Revision: 488611
- adding missing buildrequires:
- update to 1.06

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-1mdv2010.0
+ Revision: 407778
- rebuild using %%perl_convert_version

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2009.1
+ Revision: 309307
- update to new version 1.05

* Wed Jun 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2009.0
+ Revision: 228892
- update to new version 1.04

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2009.0
+ Revision: 194857
- update to new version 1.03
- update to new version 1.03

* Thu Feb 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2008.1
+ Revision: 175982
- new version

* Mon Feb 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2008.1
+ Revision: 174661
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.9-1mdv2008.0
+ Revision: 20161
- 0.9


* Thu Jan 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6-1mdk
- New release 0.6
- Add BuildRequire
- Fix source url
- use mkrel

* Sat Dec 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.5-1mdk
- Initial MDV package



