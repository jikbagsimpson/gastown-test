package tests

import (
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
