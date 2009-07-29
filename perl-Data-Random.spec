%define upstream_name    Data-Random
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Data::Random - Perl module to generate random data
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Date-Calc
BuildRequires:	perl-GD
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
A module used to generate random data.  Useful mostly for test
programs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README*
%dir %{perl_vendorlib}/Data/Random
%{perl_vendorlib}/Data/Random.pm
%{perl_vendorlib}/Data/Random/*
%{_mandir}/*/*
