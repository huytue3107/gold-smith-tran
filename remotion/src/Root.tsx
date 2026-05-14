import React from "react";
import { Composition, staticFile } from "remotion";
import { MarketReading } from "./compositions/market-reading/MarketReading";
import { marketReadingSchema } from "./compositions/market-reading/schema";
import defaultBrief from "../briefs/2026-05-14-sample-market-reading.json";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* 60s vertical 1080x1920 for TikTok/Reels/Shorts */}
      <Composition
        id="MarketReading"
        component={MarketReading}
        durationInFrames={30 * 60}
        fps={30}
        width={1080}
        height={1920}
        schema={marketReadingSchema}
        defaultProps={
          defaultBrief as React.ComponentProps<typeof MarketReading>
        }
      />
    </>
  );
};
