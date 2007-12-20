%define real_name Data-Random

Summary:	Data::Random - Perl module to generate random data
Name:		perl-%{real_name}
Version:	0.05
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-GD
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A module used to generate random data.  Useful mostly for test
programs.

%prep
%setup -q -n %{real_name}-%{version} 

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

