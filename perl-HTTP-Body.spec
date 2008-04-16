%define	module	HTTP-Body
%define	name	perl-%{module}
%define version 1.03
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	HTTP Body Parser
License:	GPL or Artistic
Group:		Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/HTTP/%{module}-%{version}.tar.gz
BuildRequires:  perl(YAML)
BuildRequires:  perl(HTTP::Headers)
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
Perl module to parse HTTP request bodies.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean 
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/HTTP/Body/*
%{perl_vendorlib}/HTTP/Body.pm
%{_mandir}/man3/*

