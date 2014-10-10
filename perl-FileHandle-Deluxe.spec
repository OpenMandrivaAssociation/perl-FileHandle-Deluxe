%define real_name FileHandle-Deluxe

Summary:	FileHandle-Deluxe module for perl 
Name:		perl-%{real_name}
Version:	0.92
Release:	6
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
FileHandle::Deluxe works like a regular FileHandle object, with the
addition of doing the routine file handle chores for you.
FileHandle::Deluxe (FD) is targeted at beginning Perl users who usually
find those tasks intimidating and often elect to skip them rather than
learn how to do them. FileHandle::Deluxe defaults to a set of best
practices for working with file handles.

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
%doc README
%{perl_vendorlib}/FileHandle/Deluxe.pm
%{_mandir}/*/*




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.92-5mdv2010.0
+ Revision: 430455
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.92-4mdv2009.0
+ Revision: 241217
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.92-2mdv2008.0
+ Revision: 86404
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.92-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.92-1mdk
- initial Mandriva package

