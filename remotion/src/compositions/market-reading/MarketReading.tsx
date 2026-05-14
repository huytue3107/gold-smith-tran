import React from "react";
import {
  AbsoluteFill,
  Sequence,
  useCurrentFrame,
  interpolate,
  spring,
  useVideoConfig,
} from "remotion";
import type { MarketReadingProps } from "./schema";

const COLORS = {
  bg: "#F5F3EE",
  ink: "#151515",
  accent: "#C6A15B",
  mute: "#6F6F6F",
};

const FRAME_HOOK_END = 30 * 5; // 5s
const FRAME_CONTEXT_END = 30 * 25; // 5-25s
const FRAME_TAKEAWAY_END = 30 * 50; // 25-50s
const FRAME_CTA_END = 30 * 60; // 50-60s

const FadeUp: React.FC<{
  from: number;
  children: React.ReactNode;
  durationFrames?: number;
}> = ({ from, children, durationFrames = 15 }) => {
  const frame = useCurrentFrame();
  const local = frame - from;
  const opacity = interpolate(local, [0, durationFrames], [0, 1], {
    extrapolateRight: "clamp",
    extrapolateLeft: "clamp",
  });
  const ty = interpolate(local, [0, durationFrames], [40, 0], {
    extrapolateRight: "clamp",
    extrapolateLeft: "clamp",
  });
  return (
    <div style={{ opacity, transform: `translateY(${ty}px)` }}>{children}</div>
  );
};

export const MarketReading: React.FC<MarketReadingProps> = ({
  hook,
  context,
  takeaway,
  cta,
  brandMark,
  pillar,
  safetyDisclaimer,
}) => {
  const { fps } = useVideoConfig();
  const frame = useCurrentFrame();
  const brandFade = spring({ frame, fps, config: { damping: 200 } });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: COLORS.bg,
        fontFamily: 'Inter, "Be Vietnam Pro", system-ui, sans-serif',
        padding: 80,
        color: COLORS.ink,
      }}
    >
      {/* Brand mark — top */}
      <div
        style={{
          opacity: brandFade,
          fontSize: 28,
          letterSpacing: 4,
          color: COLORS.mute,
          textAlign: "center",
          fontWeight: 500,
        }}
      >
        {brandMark}
      </div>
      <div
        style={{
          marginTop: 8,
          fontSize: 20,
          letterSpacing: 2,
          color: COLORS.accent,
          textAlign: "center",
          textTransform: "uppercase",
        }}
      >
        {pillar}
      </div>

      {/* Sequence 1: Hook (0-5s) */}
      <Sequence from={0} durationInFrames={FRAME_HOOK_END}>
        <AbsoluteFill
          style={{
            padding: 80,
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <FadeUp from={0}>
            <div
              style={{
                fontSize: 84,
                lineHeight: 1.15,
                fontWeight: 700,
                textAlign: "center",
                maxWidth: 900,
              }}
            >
              {hook}
            </div>
          </FadeUp>
        </AbsoluteFill>
      </Sequence>

      {/* Sequence 2: Context (5-25s) */}
      <Sequence
        from={FRAME_HOOK_END}
        durationInFrames={FRAME_CONTEXT_END - FRAME_HOOK_END}
      >
        <AbsoluteFill
          style={{
            padding: 100,
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <FadeUp from={FRAME_HOOK_END}>
            <div
              style={{
                fontSize: 56,
                lineHeight: 1.35,
                fontWeight: 500,
                textAlign: "center",
                maxWidth: 880,
                color: COLORS.ink,
              }}
            >
              {context}
            </div>
          </FadeUp>
        </AbsoluteFill>
      </Sequence>

      {/* Sequence 3: Takeaway (25-50s) */}
      <Sequence
        from={FRAME_CONTEXT_END}
        durationInFrames={FRAME_TAKEAWAY_END - FRAME_CONTEXT_END}
      >
        <AbsoluteFill
          style={{
            padding: 100,
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <FadeUp from={FRAME_CONTEXT_END}>
            <div
              style={{
                fontSize: 64,
                lineHeight: 1.25,
                fontWeight: 700,
                textAlign: "center",
                maxWidth: 900,
                borderLeft: `6px solid ${COLORS.accent}`,
                paddingLeft: 32,
              }}
            >
              {takeaway}
            </div>
          </FadeUp>
        </AbsoluteFill>
      </Sequence>

      {/* Sequence 4: CTA (50-60s) */}
      <Sequence
        from={FRAME_TAKEAWAY_END}
        durationInFrames={FRAME_CTA_END - FRAME_TAKEAWAY_END}
      >
        <AbsoluteFill
          style={{
            padding: 100,
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <FadeUp from={FRAME_TAKEAWAY_END}>
            <div style={{ textAlign: "center", maxWidth: 880 }}>
              <div
                style={{
                  fontSize: 48,
                  fontWeight: 600,
                  marginBottom: 32,
                  color: COLORS.ink,
                }}
              >
                {cta}
              </div>
              <div
                style={{
                  fontSize: 24,
                  color: COLORS.mute,
                  fontStyle: "italic",
                }}
              >
                {safetyDisclaimer}
              </div>
            </div>
          </FadeUp>
        </AbsoluteFill>
      </Sequence>
    </AbsoluteFill>
  );
};
