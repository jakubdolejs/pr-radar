"""Render icon/radar.svg into 'icon/PR Radar.icns'. Needs macOS (AppKit via pyobjc, iconutil)."""
import subprocess
import tempfile
from pathlib import Path

from AppKit import NSBitmapImageRep, NSGraphicsContext, NSImage, NSPNGFileType
from Foundation import NSMakeRect

here = Path(__file__).parent
svg = NSImage.alloc().initWithContentsOfFile_(str(here / "radar.svg"))


def png(size, path):
    rep = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(
        None, size, size, 8, 4, True, False, "NSDeviceRGBColorSpace", 0, 0)
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.setCurrentContext_(NSGraphicsContext.graphicsContextWithBitmapImageRep_(rep))
    svg.drawInRect_(NSMakeRect(0, 0, size, size))
    NSGraphicsContext.restoreGraphicsState()
    rep.representationUsingType_properties_(NSPNGFileType, {}).writeToFile_atomically_(str(path), True)


with tempfile.TemporaryDirectory() as tmp:
    iconset = Path(tmp) / "PR Radar.iconset"
    iconset.mkdir()
    for base in (16, 32, 128, 256, 512):
        png(base, iconset / f"icon_{base}x{base}.png")
        png(base * 2, iconset / f"icon_{base}x{base}@2x.png")
    subprocess.run(["iconutil", "-c", "icns", str(iconset), "-o", str(here / "PR Radar.icns")], check=True)
print("wrote", here / "PR Radar.icns")
