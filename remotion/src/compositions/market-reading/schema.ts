import { z } from "zod";

export const marketReadingSchema = z.object({
  slug: z.string(),
  date: z.string(),
  persona: z.enum([
    "F0",
    "GenZ-Millennial",
    "PhuNu-GiaDinh",
    "Founder-Fintech",
  ]),
  pillar: z.string(),
  hook: z.string().min(8).max(120),
  context: z.string().max(220),
  takeaway: z.string().max(180),
  cta: z.string().max(80),
  brandMark: z.string().default("GOLD SMITH TRAN — NHA GIA KIM TAI CHINH"),
  safetyDisclaimer: z
    .string()
    .default("Khong phai khuyen nghi dau tu. Quan tri von la viec cua ban."),
});

export type MarketReadingProps = z.infer<typeof marketReadingSchema>;
