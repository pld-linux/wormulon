Summary:	Utility to showing the current incoming/outgoing traffic.
Summary(pl):	Narzêdzie pokazuj±ce aktualny traffic.
Name:		wormulon
Version:	0.1.4
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.raisdorf.net/files/wormulon/%{name}-%{version}.tar.gz
# Source0-md5:	2ec78110fae31ee7f3cc651334da6b0e
URL:		http://www.raisdorf.net/wormulon/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wormulon is a program showing the current incoming/outgoing traffic in
one line suitable for inclusion in the screen hardstatus line.

%description -l pl
Wormulon jest programem pokazuj±cym aktualny przychodz±cy i wychodz±cy
traffic.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}

install	wormulon $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
