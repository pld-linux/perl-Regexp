#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Regexp
Summary:	Regexp Perl module - object-oriented interface to regexp code
Summary(pl):	Modu� Perla Regexp - obiektowy interfejs do wyra�e� regularnych
Name:		perl-Regexp
Version:	0.004
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	c3be11e25ec4a0cffdb163e91a10f74e
Patch0:		%{name}-perl5.8.patch
BuildRequires:	perl >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an experimental object-oriented interface to Perl's internal
regular expression code.

%description -l pl
To jest eksperymentalny zorientowany obiektowo interfejs do wyra�e�
regularnych wbudowanych w Perla.

%prep
%setup -q -n %{pdir}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Regexp.pm
# %{perl_vendorarch}/auto/Regexp dir shared with other arch-dep. Regexp::*
%{perl_vendorarch}/auto/Regexp/Regexp.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Regexp/Regexp.so
%{_mandir}/man3/*
