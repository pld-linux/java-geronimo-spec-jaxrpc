#
# Conditional build:
%if "%{pld_release}" == "ti"
%bcond_without	java_sun	# build with gcj
%else
%bcond_with	java_sun	# build with java-sun
%endif
#
%define		srcname		geronimo-spec-jaxrpc
%include	/usr/lib/rpm/macros.java
Summary:	Geronimo spec jaxrpc
Name:		java-geronimo-spec-jaxrpc
Version:	1.1
Release:	0.1
License:	Apache v2.0
Group:		Libraries/Java
# svn export http://svn.apache.org/repos/asf/geronimo/specs/branches/1_1/geronimo-spec-jaxrpc java-greonimo-spec-jaxrpc-1.1
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	630138565166448cd8190d2a82356dce
URL:		http://svn.clazzes.org/svn/odtransform/
BuildRequires:	jar
%{!?with_java_sun:BuildRequires:	java-gcj-compat-devel}
BuildRequires:	servletapi
%{?with_java_sun:BuildRequires:	java-sun >= 1.5}
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	servletapi
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Geronimo spec jaxrpc.

%prep
%setup -q

%build
required_jars="servlet-api"
CLASSPATH=$(build-classpath $required_jars)
find -name '*.java' | xargs %javac -cp $CLASSPATH
cd src
find -name '*.class' | xargs %jar cf ../%{srcname}-%{version}.jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
cp -a %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar
