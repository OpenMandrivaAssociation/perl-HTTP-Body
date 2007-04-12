%define	module	HTTP-Body
%define	name	perl-%{module}
%define version 0.6
%define release %mkrel 1

Summary:	HTTP Body Parser
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHANSEN/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
BuildRequires:  perl-YAML
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch

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

