package tests

import (
	"regexp"
	"testing"

	"github.com/jikbagsimpson/gastown-test/src"
)

func TestVersion(t *testing.T) {
	v := src.Version()
	if v == "" {
		t.Fatal("Version() returned empty string")
	}
	if v != "0.1.0" {
		t.Fatalf("Version() = %q, want %q", v, "0.1.0")
	}
}

func TestVersionSemver(t *testing.T) {
	v := src.Version()
	semver := regexp.MustCompile(`^\d+\.\d+\.\d+$`)
	if !semver.MatchString(v) {
		t.Fatalf("Version() = %q, does not match semver format X.Y.Z", v)
	}
}

func TestVersionConsistency(t *testing.T) {
	v1 := src.Version()
	v2 := src.Version()
	if v1 != v2 {
		t.Fatalf("Version() not consistent: first call = %q, second call = %q", v1, v2)
	}
}
