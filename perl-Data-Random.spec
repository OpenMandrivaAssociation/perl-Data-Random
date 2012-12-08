%define upstream_name    Data-Random
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Data::Random - Perl module to generate random data
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Date-Calc
BuildRequires:	perl-GD
BuildRequires:	perl-YAML-Tiny
BuildRequires:	perl-devel
BuildArch:	noarch

%description
A module used to generate random data.  Useful mostly for test
programs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README*
%dir %{perl_vendorlib}/Data/Random
%{perl_vendorlib}/Data/Random.pm
%{perl_vendorlib}/Data/Random/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-2
+ Revision: 765537
- rebuilt for perl-5.14.2

* Wed Jan 11 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.60.0-1
+ Revision: 759747
- BR fix
- from bz2 archive to gz
- version upadte 0.06

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2
+ Revision: 681380
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 403057
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.05-4mdv2009.0
+ Revision: 256476
- rebuild

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 0.05-2mdv2008.1
+ Revision: 135831
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-2mdv2008.0
+ Revision: 86327
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.05-1mdv2007.0
- rebuild

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.05-1mdk
- initial Mandriva package

