import {continueRender, delayRender, staticFile} from 'remotion';

// Be Vietnam Pro — weights 400/500/600/700, subsets latin + vietnamese.
// Files live in remotion/public/fonts/be-vietnam-pro/.
// Use `staticFile(...)` so the URL works in both studio and renders.

const FONT_FAMILY = 'Be Vietnam Pro';

type Subset = 'latin' | 'vietnamese';
type Weight = 400 | 500 | 600 | 700;

const SUBSET_UNICODE_RANGE: Record<Subset, string> = {
  latin:
    'U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD',
  vietnamese:
    'U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB',
};

const buildFontFace = (weight: Weight, subset: Subset): FontFace => {
  const url = staticFile(`fonts/be-vietnam-pro/be-vietnam-pro-${weight}-${subset}.woff2`);
  return new FontFace(FONT_FAMILY, `url(${url}) format('woff2')`, {
    weight: String(weight),
    style: 'normal',
    display: 'swap',
    unicodeRange: SUBSET_UNICODE_RANGE[subset],
  });
};

let loaded = false;

export const loadBeVietnamPro = (): void => {
  if (loaded || typeof document === 'undefined') {
    return;
  }
  loaded = true;

  const handle = delayRender('Loading Be Vietnam Pro');

  const weights: Weight[] = [400, 500, 600, 700];
  const subsets: Subset[] = ['latin', 'vietnamese'];

  const allFaces: FontFace[] = [];
  for (const weight of weights) {
    for (const subset of subsets) {
      const face = buildFontFace(weight, subset);
      allFaces.push(face);
      document.fonts.add(face);
    }
  }

  Promise.all(allFaces.map((f) => f.load()))
    .then(() => continueRender(handle))
    .catch((err) => {
      // Fall back silently to system fonts; do not block render.
      console.warn('Be Vietnam Pro failed to load:', err);
      continueRender(handle);
    });
};
