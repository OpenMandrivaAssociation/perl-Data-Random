%define modname	Data-Random
%define modver 0.11

Summary:	Data::Random - Perl module to generate random data
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Data/Data-Random-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-GD
BuildRequires:	perl-YAML-Tiny
BuildRequires:	perl-devel

%description
A module used to generate random data.  Useful mostly for test
programs.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README*
%dir %{perl_vendorlib}/Data/Random
%{perl_vendorlib}/Data/Random.pm
%{perl_vendorlib}/Data/Random/*
%{_mandir}/man3/*


