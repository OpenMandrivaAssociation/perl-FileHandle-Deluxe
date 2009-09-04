%define real_name FileHandle-Deluxe

Summary:	FileHandle-Deluxe module for perl 
Name:		perl-%{real_name}
Version:	0.92
Release:	%mkrel 5
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


