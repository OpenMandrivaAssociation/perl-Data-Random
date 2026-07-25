%define modname	Data-Random
%define modver 0.15

Summary:	Data::Random - Perl module to generate random data
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/barefootcoder/Data-Random
Source0:	https://cpan.metacpan.org/authors/id/B/BA/BAREFOOT/Data-Random-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-GD
BuildRequires:	perl-YAML-Tiny
BuildRequires:	perl-devel
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(File::ShareDir::Install)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::Piece)
BuildRequires:	perl(Time::MockTime)

%description
A module used to generate random data.  Useful mostly for test
programs.

%prep
%autosetup -n %{modname}-%{modver} -p1

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
