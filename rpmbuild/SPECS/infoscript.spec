Name:           infoscript
Version:        0.1.1
Release:        1%{?dist}
Summary:        This is infoscript that shows simple information about your machine

License:        GPLv3+
URL:            https//:www.anonworldwide.com/%{name}
Source0:        https//:www.anonworldwide.com/%{name}/releases/%{name}-%{version}.tar.gz

Requires:       bash
BuildArch:	noarch

%description	
This is description of our infoscript 
bash file.


%prep		
%setup -q


%build


%install

mkdir -p %{buildroot}/%{_bindir}

install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}



%changelog
