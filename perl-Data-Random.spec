%define modname	Data-Random
%define modver 0.13

Summary:	Data::Random - Perl module to generate random data
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Data/Data-Random-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-GD
BuildRequires:	perl-YAML-Tiny
BuildRequires:	perl-devel
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(File::ShareDir::Install)

%description
A module used to generate random data.  Useful mostly for test
programs.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes README*
%dir %{perl_vendorlib}/Data/Random
%{perl_vendorlib}/Data/Random.pm
%{perl_vendorlib}/Data/Random/*
%{_mandir}/man3/*


