# $Id$
# Authority: dag
# Upstream: Tatsuhiko Miyagawa <miyagawa@bulknews.net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-tag

Summary: Perl module to tag URI Scheme (RFC 4151)
Name: perl-URI-tag
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-tag/

Source: http://www.cpan.org/modules/by-module/URI/URI-tag-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Filter::Util::Call)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
Requires: perl(Filter::Util::Call)
Requires: perl(URI)

%filter_from_requires /^perl*/d
%filter_setup


%description
perl-URI-tag is a Perl module to tag URI Scheme (RFC 4151).

This package contains the following Perl module:

    URI::tag

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/URI::tag.3pm*
%dir %{perl_vendorlib}/URI/
#%{perl_vendorlib}/URI/tag/
%{perl_vendorlib}/URI/tag.pm

%changelog
* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 0.02-1
- Updated to version 0.02.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
