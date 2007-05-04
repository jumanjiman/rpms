# $Id$
# Authority: dag
# Upstream: Adam Kennedy, L<http://ali.as/>, cpan@ali.as

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name prefork

Summary: Optimized module loading for forking or non-forking processes
Name: perl-prefork
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/prefork/

Source: http://www.cpan.org/authors/id/A/AD/ADAMK/prefork-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005 
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(File::Spec) >= 0.8

%description
Optimized module loading for forking or non-forking processes.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/prefork.3pm*
%{perl_vendorlib}/prefork.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
